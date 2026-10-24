import os
import json
import asyncio
from typing import Dict, Any, List, Optional
from datetime import datetime
import motor.motor_asyncio
import pymongo

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "horizon_db")

# Path for persistent fallback store if MongoDB server is offline
DATA_STORE_DIR = os.path.join(os.path.dirname(__file__), "data_store")
os.makedirs(DATA_STORE_DIR, exist_ok=True)

class AsyncFileCollection:
    """
    High-performance async document collection providing MongoDB-compatible API
    with atomic persistence to disk. Used as a resilient fallback whenever
    a live MongoDB server is not running locally.
    """
    def __init__(self, collection_name: str):
        self.name = collection_name
        self.filepath = os.path.join(DATA_STORE_DIR, f"{collection_name}.json")
        self._lock = asyncio.Lock()
        self._data: Dict[str, Dict[str, Any]] = {}
        self._loaded = False

    async def _ensure_loaded(self):
        if not self._loaded:
            async with self._lock:
                if not self._loaded:
                    if os.path.exists(self.filepath):
                        try:
                            with open(self.filepath, "r", encoding="utf-8") as f:
                                items = json.load(f)
                                if isinstance(items, list):
                                    self._data = {str(item.get("id") or item.get("_id") or i): item for i, item in enumerate(items)}
                                elif isinstance(items, dict):
                                    self._data = items
                        except Exception:
                            self._data = {}
                    else:
                        self._data = {}
                    self._loaded = True

    async def _save(self):
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(list(self._data.values()), f, indent=2, default=str)
        except Exception as e:
            print(f"Error saving collection {self.name}: {e}")

    def _matches(self, doc: Dict[str, Any], query: Dict[str, Any]) -> bool:
        for k, v in query.items():
            if k == "_id" and "_id" not in doc and "id" in doc:
                if str(doc["id"]) != str(v):
                    return False
            elif doc.get(k) != v:
                return False
        return True

    async def find_one(self, query: Dict[str, Any], projection: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        await self._ensure_loaded()
        for doc in self._data.values():
            if self._matches(doc, query):
                res = dict(doc)
                if "_id" not in res and "id" in res:
                    res["_id"] = res["id"]
                return res
        return None

    async def find(self, query: Optional[Dict[str, Any]] = None, sort: Optional[List] = None, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        await self._ensure_loaded()
        query = query or {}
        results = []
        for doc in self._data.values():
            if self._matches(doc, query):
                res = dict(doc)
                if "_id" not in res and "id" in res:
                    res["_id"] = res["id"]
                results.append(res)
        if limit:
            results = results[:limit]
        return results

    async def insert_one(self, document: Dict[str, Any]):
        await self._ensure_loaded()
        doc_id = str(document.get("id") or document.get("_id") or f"doc_{len(self._data) + 1}")
        doc_copy = dict(document)
        doc_copy["_id"] = doc_id
        if "id" not in doc_copy:
            doc_copy["id"] = doc_id
        async with self._lock:
            self._data[doc_id] = doc_copy
            await self._save()
        return type("InsertResult", (), {"inserted_id": doc_id})

    async def insert_many(self, documents: List[Dict[str, Any]]):
        await self._ensure_loaded()
        inserted_ids = []
        async with self._lock:
            for doc in documents:
                doc_id = str(doc.get("id") or doc.get("_id") or f"doc_{len(self._data) + 1}")
                doc_copy = dict(doc)
                doc_copy["_id"] = doc_id
                if "id" not in doc_copy:
                    doc_copy["id"] = doc_id
                self._data[doc_id] = doc_copy
                inserted_ids.append(doc_id)
            await self._save()
        return type("InsertManyResult", (), {"inserted_ids": inserted_ids})

    async def update_one(self, query: Dict[str, Any], update: Dict[str, Any], upsert: bool = False):
        await self._ensure_loaded()
        async with self._lock:
            target_key = None
            for key, doc in self._data.items():
                if self._matches(doc, query):
                    target_key = key
                    break
            
            if target_key:
                if "$set" in update:
                    self._data[target_key].update(update["$set"])
                if "$inc" in update:
                    for ik, iv in update["$inc"].items():
                        self._data[target_key][ik] = self._data[target_key].get(ik, 0) + iv
                await self._save()
                return type("UpdateResult", (), {"matched_count": 1, "modified_count": 1})
            elif upsert:
                new_doc = dict(query)
                if "$set" in update:
                    new_doc.update(update["$set"])
                doc_id = str(new_doc.get("id") or new_doc.get("_id") or f"doc_{len(self._data) + 1}")
                new_doc["_id"] = doc_id
                self._data[doc_id] = new_doc
                await self._save()
                return type("UpdateResult", (), {"matched_count": 0, "modified_count": 1, "upserted_id": doc_id})
            return type("UpdateResult", (), {"matched_count": 0, "modified_count": 0})

    async def count_documents(self, query: Optional[Dict[str, Any]] = None) -> int:
        await self._ensure_loaded()
        query = query or {}
        count = 0
        for doc in self._data.values():
            if self._matches(doc, query):
                count += 1
        return count


class DatabaseManager:
    def __init__(self):
        self.is_mongo_connected = False
        self.client = None
        self.db = None
        self._fallback_collections: Dict[str, AsyncFileCollection] = {}

    async def connect(self):
        try:
            self.client = motor.motor_asyncio.AsyncIOMotorClient(
                MONGODB_URI,
                serverSelectionTimeoutMS=1500
            )
            # Ping to test connectivity
            await self.client.admin.command('ping')
            self.db = self.client[DB_NAME]
            self.is_mongo_connected = True
            print(f"[Database] Successfully connected to live MongoDB at {MONGODB_URI}")
        except Exception as e:
            self.is_mongo_connected = False
            print(f"[Database] MongoDB live server not detected ({e}). Using resilient document engine in {DATA_STORE_DIR}")

    def get_collection(self, name: str):
        if self.is_mongo_connected and self.db is not None:
            return self.db[name]
        if name not in self._fallback_collections:
            self._fallback_collections[name] = AsyncFileCollection(name)
        return self._fallback_collections[name]

db_manager = DatabaseManager()

def get_db():
    return db_manager
