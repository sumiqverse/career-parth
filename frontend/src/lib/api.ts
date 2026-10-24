const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export interface UserProfile {
  id: string;
  email: string;
  full_name: string;
  avatar?: string;
  created_at: string;
  primary_domain?: string | null;
  xp: number;
  streak: number;
  level: number;
  badges: string[];
}

export interface RoadmapSummary {
  id: string;
  slug: string;
  title: string;
  tagline: string;
  description: string;
  domain: string;
  icon: string;
  gradient: string;
  difficulty: string;
  estimated_hours: number;
  total_xp: number;
  source_attribution: string;
  stages: Array<{
    id: string;
    order: number;
    title: string;
    description: string;
    topics: Array<{
      id: string;
      title: string;
      description: string;
      duration_mins: number;
      xp: number;
      is_completed?: boolean;
    }>;
  }>;
}

export interface AssessmentQuestion {
  id: number;
  question: string;
  category: string;
  options: Array<{
    id: string;
    text: string;
    domain_scores: Record<string, number>;
  }>;
}

export interface TopicDetailPayload {
  id: string;
  roadmap_slug: string;
  stage_id: string;
  title: string;
  description: string;
  lectures: Array<{
    id: string;
    title: string;
    provider: string;
    video_url: string;
    duration: string;
    summary: string;
    key_takeaways: string[];
  }>;
  notes: string;
  questions: Array<{
    id: string;
    question: string;
    options: string[];
    correct_option: number;
    explanation: string;
    xp: number;
  }>;
  lab: {
    id: string;
    title: string;
    instructions: string;
    language: string;
    starter_code: string;
    test_cases: Array<{
      input: string;
      expected: string;
      description: string;
    }>;
    hint: string;
    xp: number;
  };
  workshop: {
    id: string;
    title: string;
    tagline: string;
    overview: string;
    steps: string[];
    acceptance_criteria: string[];
    xp: number;
  };
}

export const authStorage = {
  getToken: (): string | null => {
    if (typeof window === "undefined") return null;
    return localStorage.getItem("horizon_token");
  },
  setToken: (token: string) => {
    if (typeof window !== "undefined") {
      localStorage.setItem("horizon_token", token);
    }
  },
  removeToken: () => {
    if (typeof window !== "undefined") {
      localStorage.removeItem("horizon_token");
      localStorage.removeItem("horizon_user");
    }
  },
  getUser: (): UserProfile | null => {
    if (typeof window === "undefined") return null;
    const userStr = localStorage.getItem("horizon_user");
    return userStr ? JSON.parse(userStr) : null;
  },
  setUser: (user: UserProfile) => {
    if (typeof window !== "undefined") {
      localStorage.setItem("horizon_user", JSON.stringify(user));
    }
  }
};

const getHeaders = () => {
  const token = authStorage.getToken();
  return {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Bearer ${token}` } : {})
  };
};

export const api = {
  // --- Auth ---
  register: async (email: string, password: string, fullName: string) => {
    try {
      const res = await fetch(`${API_BASE}/api/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password, full_name: fullName })
      });
      if (!res.ok) {
        const error = await res.json().catch(() => ({ detail: "Registration failed" }));
        throw new Error(error.detail || "Registration failed");
      }
      const data = await res.json();
      authStorage.setToken(data.access_token);
      authStorage.setUser(data.user);
      return data;
    } catch (err: any) {
      throw err;
    }
  },

  login: async (email: string, password: string) => {
    try {
      const res = await fetch(`${API_BASE}/api/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
      });
      if (!res.ok) {
        const error = await res.json().catch(() => ({ detail: "Invalid credentials" }));
        throw new Error(error.detail || "Invalid credentials");
      }
      const data = await res.json();
      authStorage.setToken(data.access_token);
      authStorage.setUser(data.user);
      return data;
    } catch (err: any) {
      throw err;
    }
  },

  getMe: async (): Promise<UserProfile | null> => {
    try {
      const res = await fetch(`${API_BASE}/api/auth/me`, {
        headers: getHeaders()
      });
      if (!res.ok) return null;
      const data = await res.json();
      authStorage.setUser(data);
      return data;
    } catch {
      return authStorage.getUser();
    }
  },

  // --- Assessment ---
  getAssessmentQuestions: async (): Promise<AssessmentQuestion[]> => {
    try {
      const res = await fetch(`${API_BASE}/api/assessment/questions`);
      if (res.ok) {
        const data = await res.json();
        return data.questions;
      }
    } catch (e) {
      console.warn("Using offline assessment questions fallback:", e);
    }
    // Safe offline fallback
    return [];
  },

  submitAssessment: async (answers: Record<string, string>) => {
    const res = await fetch(`${API_BASE}/api/assessment/submit`, {
      method: "POST",
      headers: getHeaders(),
      body: JSON.stringify({ answers })
    });
    if (!res.ok) throw new Error("Failed to submit assessment");
    return await res.json();
  },

  // --- Roadmaps ---
  getTop4Roadmaps: async (): Promise<RoadmapSummary[]> => {
    try {
      const res = await fetch(`${API_BASE}/api/roadmaps/top4`, {
        headers: getHeaders()
      });
      if (res.ok) return await res.json();
    } catch (e) {
      console.warn("Backend offline, using fallback roadmaps:", e);
    }
    return [];
  },

  getAllRoadmaps: async (): Promise<RoadmapSummary[]> => {
    try {
      const res = await fetch(`${API_BASE}/api/roadmaps`, {
        headers: getHeaders()
      });
      if (res.ok) return await res.json();
    } catch (e) {
      console.warn("Backend offline, using fallback roadmaps:", e);
    }
    return [];
  },

  getRoadmapBySlug: async (slug: string): Promise<RoadmapSummary> => {
    const res = await fetch(`${API_BASE}/api/roadmaps/${slug}`, {
      headers: getHeaders()
    });
    if (!res.ok) throw new Error("Roadmap not found");
    return await res.json();
  },

  // --- Topic Deep Learning Content ---
  getTopicDetails: async (topicId: string) => {
    const res = await fetch(`${API_BASE}/api/topics/${topicId}`, {
      headers: getHeaders()
    });
    if (!res.ok) throw new Error("Topic details not found");
    return await res.json();
  },

  // --- Progress Tracking ---
  completeProgress: async (roadmapSlug: string, topicId: string, actionType: string) => {
    const res = await fetch(`${API_BASE}/api/progress/complete`, {
      method: "POST",
      headers: getHeaders(),
      body: JSON.stringify({
        roadmap_slug: roadmapSlug,
        topic_id: topicId,
        action_type: actionType
      })
    });
    if (!res.ok) throw new Error("Failed to update progress");
    return await res.json();
  },

  getGamificationStatus: async () => {
    try {
      const res = await fetch(`${API_BASE}/api/gamification/status`, {
        headers: getHeaders()
      });
      if (res.ok) return await res.json();
    } catch (e) {
      console.warn("Gamification fetch error:", e);
    }
    return null;
  },

  // --- Lab Code Runner ---
  runLabCode: async (code: string, testCases: any[]) => {
    const res = await fetch(`${API_BASE}/api/labs/run-code`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code, test_cases: testCases })
    });
    if (!res.ok) throw new Error("Failed to execute tests");
    return await res.json();
  }
};
