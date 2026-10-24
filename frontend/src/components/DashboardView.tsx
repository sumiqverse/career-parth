"use client";

import React, { useState, useEffect } from "react";
import { RoadmapSummary, UserProfile, api } from "@/lib/api";
import { 
  Sparkles, Layers, BookOpen, Clock, Trophy, ChevronRight, 
  Flame, CheckCircle2, Search, Filter, Server, BrainCircuit, 
  Palette, CloudLightning, ShieldCheck, Play 
} from "lucide-react";

interface DashboardViewProps {
  user: UserProfile | null;
  onSelectTopic: (roadmapSlug: string, topicId: string) => void;
  onStartAssessment: () => void;
}

export const DashboardView: React.FC<DashboardViewProps> = ({
  user,
  onSelectTopic,
  onStartAssessment
}) => {
  const [top4Roadmaps, setTop4Roadmaps] = useState<RoadmapSummary[]>([]);
  const [allRoadmaps, setAllRoadmaps] = useState<RoadmapSummary[]>([]);
  const [selectedRoadmap, setSelectedRoadmap] = useState<RoadmapSummary | null>(null);
  const [filterDomain, setFilterDomain] = useState<string>("all");
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadRoadmaps = async () => {
      try {
        setLoading(true);
        const [top4, all] = await Promise.all([
          api.getTop4Roadmaps(),
          api.getAllRoadmaps()
        ]);
        setTop4Roadmaps(top4);
        setAllRoadmaps(all);
        if (top4.length > 0 && !selectedRoadmap) {
          setSelectedRoadmap(top4[0]);
        }
      } catch (e) {
        console.error("Error loading roadmaps:", e);
      } finally {
        setLoading(false);
      }
    };
    loadRoadmaps();
  }, []);

  const getDomainIcon = (domain: string) => {
    switch (domain) {
      case "fullstack": return <Layers className="w-5 h-5 text-indigo-400" />;
      case "backend": return <Server className="w-5 h-5 text-teal-400" />;
      case "ai_ml": return <BrainCircuit className="w-5 h-5 text-cyan-400" />;
      case "frontend": return <Palette className="w-5 h-5 text-amber-400" />;
      case "devops": return <CloudLightning className="w-5 h-5 text-blue-400" />;
      case "cybersecurity": return <ShieldCheck className="w-5 h-5 text-rose-400" />;
      default: return <Layers className="w-5 h-5 text-indigo-400" />;
    }
  };

  const filteredAllRoadmaps = allRoadmaps.filter((rm) => {
    const matchesDomain = filterDomain === "all" || rm.domain === filterDomain;
    const matchesSearch = 
      rm.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      rm.description.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesDomain && matchesSearch;
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      
      {/* Top Banner / Welcome HUD */}
      <div className="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900/90 via-indigo-950/40 to-slate-900/90 border border-slate-800 shadow-2xl mb-12 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <span className="text-xs font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2.5 py-0.5 rounded-full border border-indigo-500/20">
              Personalized Dashboard
            </span>
            {user?.primary_domain && (
              <span className="text-xs font-semibold text-emerald-300 bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20 flex items-center gap-1">
                <CheckCircle2 className="w-3.5 h-3.5" />
                Track: {user.primary_domain.toUpperCase()}
              </span>
            )}
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-white">
            Welcome, {user?.full_name || "Developer"} 👋
          </h1>
          <p className="text-sm text-slate-400 mt-1 max-w-xl">
            Here are your **Top 4 Curated Roadmaps** and course modules. Pick any topic below to access lectures, notes, interactive quizzes, labs, and capstone workshops.
          </p>
        </div>

        {/* Quick Diagnostic Callout if not yet completed */}
        {!user?.primary_domain && (
          <button
            onClick={onStartAssessment}
            className="px-5 py-3 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-500 hover:from-indigo-500 hover:to-cyan-400 text-white font-bold text-xs sm:text-sm shadow-lg shadow-indigo-600/30 flex items-center gap-2 whitespace-nowrap transition-all"
          >
            <Sparkles className="w-4 h-4 text-cyan-200" />
            <span>Take 15-Q Diagnostic</span>
          </button>
        )}
      </div>

      {/* SECTION 1: TOP 4 RECOMMENDED ROADMAPS */}
      <div className="mb-14">
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400">
              <Sparkles className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-xl sm:text-2xl font-bold text-white">
                Top 4 Recommended Roadmaps
              </h2>
              <p className="text-xs sm:text-sm text-slate-400">
                Ranked by your cognitive preferences and roadmap.sh structures
              </p>
            </div>
          </div>
          <span className="text-xs font-medium text-slate-400 hidden sm:inline">
            Directly mapped to freeCodeCamp & Boot.dev labs
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {top4Roadmaps.map((rm, idx) => {
            const isSelected = selectedRoadmap?.slug === rm.slug;
            return (
              <div
                key={rm.slug}
                onClick={() => setSelectedRoadmap(rm)}
                className={`relative p-6 rounded-2xl border cursor-pointer transition-all flex flex-col justify-between ${
                  isSelected
                    ? "bg-slate-900 border-indigo-500 shadow-xl shadow-indigo-500/10 -translate-y-1"
                    : "bg-slate-900/60 border-slate-800 hover:border-slate-700 hover:bg-slate-900/90"
                }`}
              >
                {/* Ranking Tag */}
                <div className="flex items-center justify-between mb-4">
                  <span className="text-[11px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                    Rank #0{idx + 1}
                  </span>
                  <div className="p-2 rounded-xl bg-slate-950 border border-slate-800">
                    {getDomainIcon(rm.domain)}
                  </div>
                </div>

                <div>
                  <h3 className="font-extrabold text-white text-base mb-1.5 line-clamp-1">
                    {rm.title}
                  </h3>
                  <p className="text-xs text-slate-400 line-clamp-2 mb-4 leading-relaxed">
                    {rm.description}
                  </p>
                </div>

                {/* Metadata & Action */}
                <div className="pt-4 border-t border-slate-800/80">
                  <div className="flex items-center justify-between text-xs text-slate-400 mb-3">
                    <span className="flex items-center gap-1">
                      <Clock className="w-3.5 h-3.5 text-slate-500" />
                      {rm.estimated_hours}h
                    </span>
                    <span className="flex items-center gap-1 font-semibold text-indigo-400">
                      <Trophy className="w-3.5 h-3.5" />
                      {rm.total_xp} XP
                    </span>
                  </div>

                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      setSelectedRoadmap(rm);
                    }}
                    className={`w-full py-2 px-3 rounded-xl text-xs font-bold flex items-center justify-center gap-1.5 transition-all ${
                      isSelected
                        ? "bg-indigo-600 hover:bg-indigo-500 text-white shadow-md shadow-indigo-600/30"
                        : "bg-slate-800 hover:bg-slate-700 text-slate-200"
                    }`}
                  >
                    <span>{isSelected ? "Active Path" : "View Stages"}</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* SELECTED ROADMAP STAGES & TOPICS VIEWER */}
      {selectedRoadmap && (
        <div className="p-6 sm:p-8 rounded-3xl bg-slate-900/80 border border-slate-800 shadow-2xl mb-16">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800 mb-6">
            <div className="flex items-center gap-3">
              <div className="p-3 rounded-2xl bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                {getDomainIcon(selectedRoadmap.domain)}
              </div>
              <div>
                <span className="text-xs font-bold text-indigo-400 uppercase tracking-wider">
                  Interactive Learning Path
                </span>
                <h3 className="text-xl sm:text-2xl font-bold text-white">
                  {selectedRoadmap.title}
                </h3>
              </div>
            </div>
            <div className="text-xs text-slate-400 bg-slate-950 px-3.5 py-1.5 rounded-xl border border-slate-800">
              {selectedRoadmap.stages.length} Stages • {selectedRoadmap.source_attribution}
            </div>
          </div>

          {/* Stages List */}
          <div className="space-y-6">
            {selectedRoadmap.stages.map((stage, stageIdx) => (
              <div key={stage.id} className="p-5 rounded-2xl bg-slate-950/70 border border-slate-800/80">
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center gap-2.5">
                    <span className="w-6 h-6 rounded-lg bg-indigo-500/20 text-indigo-300 text-xs font-bold flex items-center justify-center border border-indigo-500/30">
                      {stageIdx + 1}
                    </span>
                    <h4 className="font-bold text-white text-base">
                      {stage.title}
                    </h4>
                  </div>
                  <span className="text-xs text-slate-400">
                    {stage.topics.length} Topics
                  </span>
                </div>
                <p className="text-xs text-slate-400 mb-4">
                  {stage.description}
                </p>

                {/* Topics Grid */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  {stage.topics.map((topic) => (
                    <div
                      key={topic.id}
                      onClick={() => onSelectTopic(selectedRoadmap.slug, topic.id)}
                      className="p-3.5 rounded-xl bg-slate-900 border border-slate-800 hover:border-indigo-500/60 hover:bg-slate-850 cursor-pointer transition-all flex items-center justify-between group"
                    >
                      <div className="pr-3">
                        <h5 className="font-semibold text-sm text-slate-200 group-hover:text-indigo-300 transition-colors">
                          {topic.title}
                        </h5>
                        <span className="text-[11px] text-slate-400 flex items-center gap-2 mt-1">
                          <span>{topic.duration_mins} mins</span>
                          <span>•</span>
                          <span className="text-indigo-400 font-medium">+{topic.xp} XP</span>
                          {topic.is_completed && (
                            <>
                              <span>•</span>
                              <span className="text-emerald-400 font-semibold flex items-center gap-0.5">
                                <CheckCircle2 className="w-3 h-3" /> Done
                              </span>
                            </>
                          )}
                        </span>
                      </div>

                      <div className="w-8 h-8 rounded-lg bg-indigo-600/20 text-indigo-400 group-hover:bg-indigo-600 group-hover:text-white flex items-center justify-center transition-all flex-shrink-0">
                        <Play className="w-4 h-4 fill-current ml-0.5" />
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* SECTION 2: "SEE ALL COURSES & ROADMAPS" */}
      <div id="all-courses" className="pt-4">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400">
              <BookOpen className="w-5 h-5" />
            </div>
            <div>
              <h2 className="text-xl sm:text-2xl font-bold text-white">
                See All Courses & Roadmaps
              </h2>
              <p className="text-xs sm:text-sm text-slate-400">
                Explore the complete library across all disciplines
              </p>
            </div>
          </div>

          {/* Search Input */}
          <div className="relative w-full md:w-64">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-500" />
            <input
              type="text"
              placeholder="Search roadmaps..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-9 pr-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-xs sm:text-sm text-white placeholder-slate-500 outline-none focus:border-indigo-500 transition-all"
            />
          </div>
        </div>

        {/* Filter Pills */}
        <div className="flex flex-wrap gap-2 mb-6">
          {[
            { id: "all", label: "All Roadmaps" },
            { id: "fullstack", label: "Full Stack" },
            { id: "backend", label: "Backend" },
            { id: "ai_ml", label: "AI / ML" },
            { id: "frontend", label: "Frontend" },
            { id: "devops", label: "DevOps & Cloud" },
            { id: "cybersecurity", label: "Cyber Security" }
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setFilterDomain(tab.id)}
              className={`px-3.5 py-1.5 rounded-full text-xs font-semibold transition-all ${
                filterDomain === tab.id
                  ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/30"
                  : "bg-slate-900 text-slate-400 hover:text-slate-200 border border-slate-800"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* All Courses Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredAllRoadmaps.map((rm) => (
            <div
              key={rm.slug}
              className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 hover:border-slate-700 transition-all flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2.5 py-0.5 rounded-full border border-indigo-500/20">
                    {rm.difficulty}
                  </span>
                  {getDomainIcon(rm.domain)}
                </div>
                <h3 className="font-extrabold text-white text-lg mb-1.5">
                  {rm.title}
                </h3>
                <p className="text-xs text-slate-400 line-clamp-3 mb-4 leading-relaxed">
                  {rm.description}
                </p>
              </div>

              <div className="pt-4 border-t border-slate-800">
                <div className="flex items-center justify-between text-xs text-slate-400 mb-3">
                  <span>{rm.estimated_hours} Hours Total</span>
                  <span className="font-bold text-indigo-400">{rm.total_xp} XP</span>
                </div>
                <button
                  onClick={() => {
                    setSelectedRoadmap(rm);
                    window.scrollTo({ top: 350, behavior: "smooth" });
                  }}
                  className="w-full py-2 px-3 rounded-xl bg-slate-800 hover:bg-indigo-600 text-slate-200 hover:text-white text-xs font-bold flex items-center justify-center gap-1.5 transition-all"
                >
                  <span>Start Learning</span>
                  <ChevronRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>

    </div>
  );
};
