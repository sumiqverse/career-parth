"use client";

import React, { useState, useEffect } from "react";
import { 
  RoadmapSummary, UserProfile, api, MissionPayload, 
  MilestonePayload, JourneyPayload, ExplorationActivity 
} from "@/lib/api";
import { 
  Sparkles, Layers, BookOpen, Clock, Trophy, ChevronRight, 
  Flame, CheckCircle2, Search, Filter, Server, BrainCircuit, 
  Palette, CloudLightning, ShieldCheck, Play, Smartphone, Database, 
  Compass, Cpu, Target, Calendar, ArrowRight, Check, AlertCircle, 
  HelpCircle, Code2, RefreshCw, ThumbsUp, Send, Loader2
} from "lucide-react";
import confetti from "canvas-confetti";

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
  const [activeTab, setActiveTab] = useState<"journey" | "missions" | "explore">("journey");
  
  // Data states
  const [top4Roadmaps, setTop4Roadmaps] = useState<RoadmapSummary[]>([]);
  const [allRoadmaps, setAllRoadmaps] = useState<RoadmapSummary[]>([]);
  const [selectedRoadmap, setSelectedRoadmap] = useState<RoadmapSummary | null>(null);
  
  // Journey & Personalization states
  const [journey, setJourney] = useState<JourneyPayload | null>(null);
  const [planningHorizon, setPlanningHorizon] = useState<string>("6_months");
  const [weeklyHours, setWeeklyHours] = useState<number>(10);
  const [updatingPlanning, setUpdatingPlanning] = useState(false);

  // Missions state
  const [currentMission, setCurrentMission] = useState<MissionPayload | null>(null);
  const [completingMission, setCompletingMission] = useState(false);

  // Career Exploration Experiments state
  const [explorationTasks, setExplorationTasks] = useState<ExplorationActivity[]>([]);
  const [activeExpModal, setActiveExpModal] = useState<ExplorationActivity | null>(null);
  const [expInterest, setExpInterest] = useState<number>(5);
  const [expDifficulty, setExpDifficulty] = useState<number>(3);
  const [expWouldExplore, setExpWouldExplore] = useState<boolean>(true);
  const [expIndependent, setExpIndependent] = useState<boolean>(true);
  const [expFeedbackText, setExpFeedbackText] = useState("");
  const [submittingFeedback, setSubmittingFeedback] = useState(false);
  const [feedbackSuccess, setFeedbackSuccess] = useState(false);

  // Filter & Search
  const [filterDomain, setFilterDomain] = useState<string>("all");
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadInitialData = async () => {
      try {
        setLoading(true);
        const [top4Res, allRes, journeyRes, missionRes, expRes] = await Promise.allSettled([
          api.getTop4Roadmaps(),
          api.getAllRoadmaps(),
          api.getJourney(),
          api.getNextMission(),
          api.getExplorationActivities()
        ]);

        const top4 = top4Res.status === "fulfilled" ? top4Res.value : [];
        const all = allRes.status === "fulfilled" ? allRes.value : [];
        const journeyData = journeyRes.status === "fulfilled" ? journeyRes.value : null;
        const missionData = missionRes.status === "fulfilled" ? missionRes.value : null;
        const expTasks = expRes.status === "fulfilled" ? expRes.value : [];

        // If top4 is empty for some reason, fallback to first 4 of all
        const effectiveTop4 = top4.length > 0 ? top4 : all.slice(0, 4);
        setTop4Roadmaps(effectiveTop4);
        setAllRoadmaps(all);

        if (effectiveTop4.length > 0 && !selectedRoadmap) {
          setSelectedRoadmap(effectiveTop4[0]);
        }
        if (journeyData) {
          setJourney(journeyData);
          setPlanningHorizon(journeyData.planning_horizon || "6_months");
          setWeeklyHours(journeyData.weekly_hours || 10);
        }
        if (missionData) {
          setCurrentMission(missionData);
        }
        if (expTasks && expTasks.length > 0) {
          setExplorationTasks(expTasks);
        }
      } catch (e) {
        console.error("Error loading dashboard data:", e);
      } finally {
        setLoading(false);
      }
    };
    loadInitialData();
  }, []);


  const handlePlanningChange = async (newHorizon: string, newHours: number) => {
    setPlanningHorizon(newHorizon);
    setWeeklyHours(newHours);
    setUpdatingPlanning(true);
    try {
      const res = await api.updatePlanningHorizon(newHorizon, newHours);
      if (res.milestones && journey) {
        setJourney({
          ...journey,
          planning_horizon: newHorizon,
          weekly_hours: newHours,
          milestones: res.milestones
        });
      }
    } catch (e) {
      console.warn("Could not update planning horizon:", e);
    } finally {
      setUpdatingPlanning(false);
    }
  };

  const handleCompleteMission = async () => {
    if (!currentMission) return;
    setCompletingMission(true);
    try {
      await api.completeMission(currentMission.id, currentMission.skill_id, true);
      confetti({ particleCount: 60, spread: 70, origin: { y: 0.7 } });
      const nextMsn = await api.getNextMission();
      setCurrentMission(nextMsn);
      const updatedJourney = await api.getJourney();
      if (updatedJourney) setJourney(updatedJourney);
    } catch (e) {
      console.error("Mission complete error:", e);
    } finally {
      setCompletingMission(false);
    }
  };

  const handleSubmitExploration = async () => {
    if (!activeExpModal) return;
    setSubmittingFeedback(true);
    try {
      await api.submitExplorationFeedback({
        activity_id: activeExpModal.id,
        domain: activeExpModal.domain,
        interest_rating: expInterest,
        difficulty_rating: expDifficulty,
        would_explore_further: expWouldExplore,
        completed_independently: expIndependent,
        confusing_part: expFeedbackText || undefined
      });
      setFeedbackSuccess(true);
      confetti({ particleCount: 50, spread: 60, origin: { y: 0.6 } });
      setTimeout(() => {
        setActiveExpModal(null);
        setFeedbackSuccess(false);
        setExpFeedbackText("");
      }, 1500);
      // Refresh roadmaps and journey
      const [top4, journeyData] = await Promise.all([
        api.getTop4Roadmaps(),
        api.getJourney()
      ]);
      setTop4Roadmaps(top4);
      if (journeyData) setJourney(journeyData);
    } catch (e) {
      console.error("Failed to submit feedback:", e);
    } finally {
      setSubmittingFeedback(false);
    }
  };

  const getDomainIcon = (domain: string) => {
    switch (domain) {
      case "fullstack": return <Layers className="w-5 h-5 text-indigo-400" />;
      case "backend": return <Server className="w-5 h-5 text-teal-400" />;
      case "ai_ml": return <BrainCircuit className="w-5 h-5 text-cyan-400" />;
      case "frontend": return <Palette className="w-5 h-5 text-amber-400" />;
      case "devops": return <CloudLightning className="w-5 h-5 text-blue-400" />;
      case "cybersecurity": return <ShieldCheck className="w-5 h-5 text-rose-400" />;
      case "mobile": return <Smartphone className="w-5 h-5 text-emerald-400" />;
      case "data": return <Database className="w-5 h-5 text-teal-400" />;
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
      <div className="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900/90 via-indigo-950/40 to-slate-900/90 border border-slate-800 shadow-2xl mb-8 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
        <div>
          <div className="flex flex-wrap items-center gap-2 mb-2">
            <span className="text-xs font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2.5 py-0.5 rounded-full border border-indigo-500/20">
              Personalized Dashboard
            </span>
            {user?.archetype && (
              <span className="text-xs font-semibold text-purple-300 bg-purple-500/10 px-2.5 py-0.5 rounded-full border border-purple-500/30 flex items-center gap-1">
                🧠 Archetype: {user.archetype}
              </span>
            )}
            {user?.primary_domain && !user?.archetype && (
              <span className="text-xs font-semibold text-emerald-300 bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20 flex items-center gap-1">
                <CheckCircle2 className="w-3.5 h-3.5" />
                Track: {user.primary_domain.toUpperCase()}
              </span>
            )}
            {user?.is_exploring_mode && (
              <span className="text-xs font-semibold text-amber-300 bg-amber-500/10 px-2.5 py-0.5 rounded-full border border-amber-500/30 flex items-center gap-1">
                ✨ Adaptive Track Active
              </span>
            )}
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-white">
            Welcome, {user?.full_name || "Developer"} 👋
          </h1>
          <p className="text-sm text-slate-400 mt-1 max-w-xl">
            {user?.is_exploring_mode
              ? "We have arranged an exploratory gateway path for you. As you complete lessons, quick 5-second reflections dynamically adapt your roadmaps to what your brain loves."
              : "Continuous prerequisite-aware guidance from fundamentals to production mastery. Every mission and milestone adapts based on your demonstrated skill evidence."}
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

      {/* SECTION: DAILY ACTIONS & MASTERY QUESTS */}
      <div id="daily-actions" className="mb-10 p-6 sm:p-7 rounded-3xl bg-slate-900/70 border border-amber-500/20 shadow-xl relative overflow-hidden">
        <div className="absolute top-0 right-0 w-64 h-64 bg-amber-500/5 rounded-full blur-3xl pointer-events-none" />
        
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-2xl bg-amber-500/10 border border-amber-500/30 text-amber-400">
              <Flame className="w-6 h-6 animate-pulse" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-xl sm:text-2xl font-extrabold text-white">Daily Actions & Quests</h2>
                <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30">
                  {user?.streak || 1} Day Streak
                </span>
              </div>
              <p className="text-xs sm:text-sm text-slate-400">
                Complete daily micro-habits to lock in concepts and gain maximum XP
              </p>
            </div>
          </div>
          
          <div className="flex items-center gap-2 text-xs font-semibold text-slate-300 bg-slate-950 px-3.5 py-2 rounded-xl border border-slate-800">
            <Trophy className="w-4 h-4 text-amber-400" />
            <span>Today&apos;s Target: 100 XP</span>
          </div>
        </div>

        {/* 3 Action Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {/* Action 1: Active Topic / Practice */}
          <div className="p-4 rounded-2xl bg-slate-950/80 border border-slate-800 hover:border-indigo-500/50 transition-all flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between mb-2">
                <span className="text-[10px] font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded">
                  Action 01 • Topic Lab
                </span>
                <span className="text-xs font-bold text-indigo-300">+50 XP</span>
              </div>
              <h4 className="font-bold text-white text-sm mb-1">
                {selectedRoadmap ? `${selectedRoadmap.title} Practice` : "Core Fundamentals Lab"}
              </h4>
              <p className="text-xs text-slate-400 leading-relaxed">
                Watch curated lecture segment and solve interactive hands-on code challenges.
              </p>
            </div>
            <button
              onClick={() => {
                if (selectedRoadmap && selectedRoadmap.stages[0]?.topics[0]) {
                  onSelectTopic(selectedRoadmap.slug, selectedRoadmap.stages[0].topics[0].id);
                } else if (top4Roadmaps[0]?.stages[0]?.topics[0]) {
                  onSelectTopic(top4Roadmaps[0].slug, top4Roadmaps[0].stages[0].topics[0].id);
                }
              }}
              className="mt-4 w-full py-2 px-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold flex items-center justify-center gap-1.5 shadow-md shadow-indigo-600/20 transition-all"
            >
              <span>Launch Lab Session</span>
              <Play className="w-3.5 h-3.5 fill-current" />
            </button>
          </div>

          {/* Action 2: Diagnostic / Adaptive Reflection */}
          <div className="p-4 rounded-2xl bg-slate-950/80 border border-slate-800 hover:border-cyan-500/50 transition-all flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between mb-2">
                <span className="text-[10px] font-bold uppercase tracking-wider text-cyan-400 bg-cyan-500/10 px-2 py-0.5 rounded">
                  Action 02 • Calibration
                </span>
                <span className="text-xs font-bold text-cyan-300">+35 XP</span>
              </div>
              <h4 className="font-bold text-white text-sm mb-1">
                {user?.primary_domain ? "Adaptive Career Compass" : "15-Q Diagnostic Evaluation"}
              </h4>
              <p className="text-xs text-slate-400 leading-relaxed">
                {user?.primary_domain 
                  ? "5-second micro reflections dynamically tailor your future topics to what you enjoy."
                  : "Discover your engineering personality and uncover your top 4 career paths."}
              </p>
            </div>
            <button
              onClick={onStartAssessment}
              className="mt-4 w-full py-2 px-3 rounded-xl bg-cyan-600/20 hover:bg-cyan-600/30 text-cyan-300 border border-cyan-500/30 text-xs font-bold flex items-center justify-center gap-1.5 transition-all"
            >
              <Sparkles className="w-3.5 h-3.5" />
              <span>{user?.primary_domain ? "Calibrate Compass" : "Take Diagnostic"}</span>
            </button>
          </div>

          {/* Action 3: Daily Streak Shield */}
          <div className="p-4 rounded-2xl bg-slate-950/80 border border-slate-800 hover:border-amber-500/50 transition-all flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between mb-2">
                <span className="text-[10px] font-bold uppercase tracking-wider text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded">
                  Action 03 • Habit Loop
                </span>
                <span className="text-xs font-bold text-amber-300">+25 XP</span>
              </div>
              <h4 className="font-bold text-white text-sm mb-1">
                Maintain Your Learning Streak
              </h4>
              <p className="text-xs text-slate-400 leading-relaxed">
                Keep the momentum going. Finish 1 exercise before midnight to safeguard your streak.
              </p>
            </div>
            <div className="mt-4 flex items-center justify-between px-3 py-2 rounded-xl bg-slate-900 border border-slate-800">
              <span className="text-xs text-slate-300 font-medium flex items-center gap-1.5">
                <Flame className="w-4 h-4 text-amber-400 fill-amber-400" />
                Streak Status:
              </span>
              <span className="text-xs font-bold text-emerald-400 flex items-center gap-1">
                <CheckCircle2 className="w-3.5 h-3.5" /> Active ({user?.streak || 1}d)
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* DASHBOARD TOP LEVEL TABS: MY JOURNEY vs MY MISSIONS vs CAREER EXPLORER */}

      <div className="flex items-center gap-3 p-1.5 rounded-2xl bg-slate-900 border border-slate-800 mb-10 overflow-x-auto">
        <button
          onClick={() => setActiveTab("journey")}
          className={`flex-1 min-w-[160px] py-3 px-4 rounded-xl text-xs sm:text-sm font-bold flex items-center justify-center gap-2 transition-all ${
            activeTab === "journey"
              ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/30"
              : "text-slate-400 hover:text-slate-200"
          }`}
        >
          <Compass className="w-4 h-4" />
          <span>🧭 Tab A: My Journey</span>
        </button>

        <button
          onClick={() => setActiveTab("missions")}
          className={`flex-1 min-w-[160px] py-3 px-4 rounded-xl text-xs sm:text-sm font-bold flex items-center justify-center gap-2 transition-all relative ${
            activeTab === "missions"
              ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/30"
              : "text-slate-400 hover:text-slate-200"
          }`}
        >
          <Target className="w-4 h-4" />
          <span>🎯 Tab B: My Missions (Daily Action)</span>
          {currentMission && (
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping absolute right-3 top-3" />
          )}
        </button>

        <button
          onClick={() => setActiveTab("explore")}
          className={`flex-1 min-w-[160px] py-3 px-4 rounded-xl text-xs sm:text-sm font-bold flex items-center justify-center gap-2 transition-all ${
            activeTab === "explore"
              ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/30"
              : "text-slate-400 hover:text-slate-200"
          }`}
        >
          <BookOpen className="w-4 h-4" />
          <span>🚀 Career Explorer & Courses</span>
        </button>
      </div>

      {/* ========================================================================= */}
      {/* TAB A: MY JOURNEY (ROADMAP, HORIZON PACING, PREREQUISITES) */}
      {/* ========================================================================= */}
      {activeTab === "journey" && (
        <div id="my-journey" className="space-y-12 animate-fade-in">

          
          {/* Planning Horizon & Weekly Availability Controller Card */}
          <div className="p-6 sm:p-8 rounded-3xl bg-slate-900/80 border border-slate-800 shadow-xl">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-6 pb-6 border-b border-slate-800">
              <div>
                <span className="text-xs font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2.5 py-0.5 rounded-full border border-indigo-500/20">
                  Adaptive Time Horizon & Workload Pacing
                </span>
                <h3 className="text-xl sm:text-2xl font-bold text-white mt-2">
                  Personalized Roadmap Horizon
                </h3>
                <p className="text-xs sm:text-sm text-slate-400 mt-1">
                  Changing your horizon recalibrates milestone milestones, task granularity, and weekly study hours.
                </p>
              </div>

              {/* Weekly Availability Selector */}
              <div className="flex items-center gap-2 bg-slate-950 p-2 rounded-2xl border border-slate-800">
                <span className="text-xs text-slate-400 px-2 font-medium flex items-center gap-1">
                  <Clock className="w-3.5 h-3.5" /> Study:
                </span>
                {[5, 10, 15, 20].map((hours) => (
                  <button
                    key={hours}
                    onClick={() => handlePlanningChange(planningHorizon, hours)}
                    className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all ${
                      weeklyHours === hours
                        ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/30"
                        : "text-slate-400 hover:text-slate-200 hover:bg-slate-900"
                    }`}
                  >
                    {hours}h/wk
                  </button>
                ))}
              </div>
            </div>

            {/* Planning Horizon Pills */}
            <div className="pt-6">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-400 block mb-3">
                Select Planning Horizon:
              </span>
              <div className="grid grid-cols-2 sm:grid-cols-5 gap-3">
                {[
                  { id: "1_month", label: "1 Month", desc: "Intensive Sprint" },
                  { id: "3_months", label: "3 Months", desc: "Focused Track" },
                  { id: "6_months", label: "6 Months", desc: "Full Mastery" },
                  { id: "1_year", label: "1 Year", desc: "Mid-Level Career" },
                  { id: "4_years", label: "4 Years", desc: "CS Degree Pathway" }
                ].map((h) => {
                  const isSelected = planningHorizon === h.id;
                  return (
                    <button
                      key={h.id}
                      onClick={() => handlePlanningChange(h.id, weeklyHours)}
                      className={`p-3.5 rounded-2xl border text-left transition-all ${
                        isSelected
                          ? "bg-slate-900 border-indigo-500 ring-1 ring-indigo-500/50 shadow-lg shadow-indigo-500/20"
                          : "bg-slate-950/60 border-slate-800 hover:border-slate-700 hover:bg-slate-900/50"
                      }`}
                    >
                      <div className="font-extrabold text-white text-sm">
                        {h.label}
                      </div>
                      <div className="text-[11px] text-slate-400 mt-0.5">
                        {h.desc}
                      </div>
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Dynamic Milestone Progress Breakdown */}
            {journey && journey.milestones && (
              <div className="mt-8 pt-6 border-t border-slate-800/80">
                <div className="flex items-center justify-between mb-4">
                  <h4 className="font-bold text-white text-sm flex items-center gap-2">
                    <Target className="w-4 h-4 text-emerald-400" />
                    <span>Calculated Horizon Milestones ({journey.milestones.length} Phases):</span>
                  </h4>
                  <span className="text-xs text-indigo-400 font-semibold">
                    ~{weeklyHours * (planningHorizon === "1_month" ? 4 : planningHorizon === "3_months" ? 12 : planningHorizon === "6_months" ? 24 : planningHorizon === "1_year" ? 52 : 208)} Total Target Hours
                  </span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  {journey.milestones.map((ms, idx) => (
                    <div key={ms.id} className="p-4 rounded-2xl bg-slate-950/70 border border-slate-800 flex flex-col justify-between">
                      <div>
                        <div className="flex items-center justify-between text-xs text-slate-400 mb-2">
                          <span className="font-bold text-indigo-400">Milestone #{idx + 1}</span>
                          <span className="px-2 py-0.5 rounded-md bg-slate-900 border border-slate-800">{ms.target_hours}h</span>
                        </div>
                        <h5 className="font-bold text-white text-sm mb-1">{ms.title}</h5>
                        <p className="text-xs text-slate-400 leading-relaxed mb-3">{ms.target_outcome}</p>
                      </div>
                      <div className="flex flex-wrap gap-1.5 pt-2 border-t border-slate-900">
                        {ms.focus_skills.map((sk) => (
                          <span key={sk} className="text-[10px] px-2 py-0.5 rounded-md bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">
                            {sk.replace("skill_", "").replace(/_/g, " ")}
                          </span>
                        ))}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Top 4 Recommended Roadmaps Section */}
          <div>
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
                    Ranked by your cognitive preferences & validated roadmap.sh structures
                  </p>
                </div>
              </div>
              <span className="text-xs font-medium text-slate-400 hidden sm:inline">
                Verified GOAT Curated Resources
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
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

          {/* Selected Roadmap Stages & Topics with Prerequisite Badges */}
          {selectedRoadmap && (
            <div className="p-6 sm:p-8 rounded-3xl bg-slate-900/80 border border-slate-800 shadow-2xl">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800 mb-6">
                <div className="flex items-center gap-3">
                  <div className="p-3 rounded-2xl bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                    {getDomainIcon(selectedRoadmap.domain)}
                  </div>
                  <div>
                    <span className="text-xs font-bold text-indigo-400 uppercase tracking-wider">
                      Interactive Learning Stages
                    </span>
                    <h3 className="text-xl sm:text-2xl font-bold text-white">
                      {selectedRoadmap.title}
                    </h3>
                  </div>
                </div>
                <div className="text-xs text-slate-400 bg-slate-950 px-3.5 py-1.5 rounded-xl border border-slate-800">
                  {selectedRoadmap.stages.length} Stages • Verified GOAT Curated Resources
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
                            <h5 className="font-bold text-white text-xs sm:text-sm group-hover:text-indigo-300 transition-colors line-clamp-1">
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

        </div>
      )}

      {/* ========================================================================= */}
      {/* TAB B: MY MISSIONS (DAILY ACTION: 3-PART STRUCTURED ACTION) */}
      {/* ========================================================================= */}
      {activeTab === "missions" && (
        <div className="space-y-8 animate-fade-in">
          
          {/* Active Mission Card */}
          {currentMission ? (
            <div className="p-6 sm:p-10 rounded-3xl bg-gradient-to-br from-slate-900 via-indigo-950/30 to-slate-900 border border-indigo-500/40 shadow-2xl relative overflow-hidden">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800/80 mb-6">
                <div>
                  <div className="flex items-center gap-2 mb-2">
                    <span className="text-xs font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-300 border border-emerald-500/20 flex items-center gap-1">
                      <Target className="w-3.5 h-3.5" />
                      Immediate Recommended Action
                    </span>
                    <span className="text-xs text-slate-400">
                      ⏱️ ~{currentMission.estimated_minutes} mins total
                    </span>
                  </div>
                  <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
                    {currentMission.title}
                  </h2>
                </div>

                <button
                  onClick={handleCompleteMission}
                  disabled={completingMission}
                  className="px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-500 hover:from-emerald-500 hover:to-teal-400 text-white font-bold text-sm shadow-lg shadow-emerald-600/30 flex items-center gap-2 transition-all flex-shrink-0"
                >
                  {completingMission ? <Loader2 className="w-4 h-4 animate-spin" /> : <CheckCircle2 className="w-4 h-4" />}
                  <span>Complete Mission (+50 XP)</span>
                </button>
              </div>

              {/* Rationale explanation */}
              <div className="p-4 rounded-2xl bg-indigo-950/40 border border-indigo-500/20 mb-8 flex items-start gap-3">
                <Sparkles className="w-5 h-5 text-indigo-400 flex-shrink-0 mt-0.5" />
                <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                  <span className="font-bold text-white">Why this mission?</span> {currentMission.rationale}
                </p>
              </div>

              {/* 3-Part Micro-Learning Action Modules */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                
                {/* 1. Learn (~10m) */}
                <div className="p-5 rounded-2xl bg-slate-950/80 border border-slate-800 flex flex-col justify-between">
                  <div>
                    <div className="flex items-center justify-between text-xs text-slate-400 mb-3">
                      <span className="font-bold uppercase tracking-wider text-indigo-400">1. Learn</span>
                      <span>{currentMission.learn_module.duration}</span>
                    </div>
                    <h4 className="font-bold text-white text-base mb-2">Curated GOAT Video</h4>
                    <p className="text-xs text-slate-400 leading-relaxed">
                      {currentMission.learn_module.objective}
                    </p>
                  </div>
                  <button
                    onClick={() => onSelectTopic(selectedRoadmap?.slug || "full-stack-developer", currentMission.skill_id.replace("skill_", "fs_topic_"))}
                    className="w-full mt-4 py-2 px-3 rounded-xl bg-indigo-600/20 hover:bg-indigo-600 text-indigo-300 hover:text-white text-xs font-bold flex items-center justify-center gap-1.5 transition-all"
                  >
                    <Play className="w-3.5 h-3.5 fill-current" />
                    <span>Watch GOAT Lecture</span>
                  </button>
                </div>

                {/* 2. Practice (~15m) */}
                <div className="p-5 rounded-2xl bg-slate-950/80 border border-slate-800 flex flex-col justify-between">
                  <div>
                    <div className="flex items-center justify-between text-xs text-slate-400 mb-3">
                      <span className="font-bold uppercase tracking-wider text-teal-400">2. Practice</span>
                      <span>{currentMission.practice_module.duration}</span>
                    </div>
                    <h4 className="font-bold text-white text-base mb-2">Hands-on Code Lab</h4>
                    <p className="text-xs text-slate-400 leading-relaxed">
                      {currentMission.practice_module.instructions}
                    </p>
                  </div>
                  <button
                    onClick={() => onSelectTopic(selectedRoadmap?.slug || "full-stack-developer", currentMission.skill_id.replace("skill_", "fs_topic_"))}
                    className="w-full mt-4 py-2 px-3 rounded-xl bg-teal-600/20 hover:bg-teal-600 text-teal-300 hover:text-white text-xs font-bold flex items-center justify-center gap-1.5 transition-all"
                  >
                    <Code2 className="w-3.5 h-3.5" />
                    <span>Launch Code Editor</span>
                  </button>
                </div>

                {/* 3. Prove (~5m) */}
                <div className="p-5 rounded-2xl bg-slate-950/80 border border-slate-800 flex flex-col justify-between">
                  <div>
                    <div className="flex items-center justify-between text-xs text-slate-400 mb-3">
                      <span className="font-bold uppercase tracking-wider text-amber-400">3. Prove</span>
                      <span className="text-amber-400 font-bold">+{currentMission.prove_module.xp_reward} XP</span>
                    </div>
                    <h4 className="font-bold text-white text-base mb-2">Diagnostic Quiz</h4>
                    <p className="text-xs text-slate-400 leading-relaxed">
                      {currentMission.prove_module.quiz_question}
                    </p>
                  </div>
                  <button
                    onClick={() => onSelectTopic(selectedRoadmap?.slug || "full-stack-developer", currentMission.skill_id.replace("skill_", "fs_topic_"))}
                    className="w-full mt-4 py-2 px-3 rounded-xl bg-amber-600/20 hover:bg-amber-600 text-amber-300 hover:text-white text-xs font-bold flex items-center justify-center gap-1.5 transition-all"
                  >
                    <CheckCircle2 className="w-3.5 h-3.5" />
                    <span>Take Quiz Check</span>
                  </button>
                </div>

              </div>
            </div>
          ) : (
            <div className="p-12 text-center rounded-3xl bg-slate-900 border border-slate-800">
              <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-3" />
              <h3 className="text-lg font-bold text-white">All Active Missions Up to Date!</h3>
              <p className="text-xs text-slate-400 mt-1">Review the journey tab or explore further below.</p>
            </div>
          )}

        </div>
      )}

      {/* ========================================================================= */}
      {/* TAB C: CAREER EXPLORATION EXPERIMENTS & ALL ROADMAPS */}
      {/* ========================================================================= */}
      {activeTab === "explore" && (
        <div className="space-y-12 animate-fade-in">
          
          {/* Beginner Career Exploration Experiments Section */}
          <div className="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950/30 to-slate-900 border border-slate-800">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
              <div>
                <span className="text-xs font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2.5 py-0.5 rounded-full border border-indigo-500/20">
                  Practical Career Discovery
                </span>
                <h3 className="text-xl sm:text-2xl font-bold text-white mt-1">
                  15-Minute Beginner Exploration Experiments
                </h3>
                <p className="text-xs sm:text-sm text-slate-400 mt-0.5">
                  Try practical activities before committing to a career path. Your feedback automatically adjusts recommendation weights.
                </p>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {explorationTasks.map((act) => (
                <div
                  key={act.id}
                  className="p-5 rounded-2xl bg-slate-950/80 border border-slate-800 flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between mb-3">
                      <span className="text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">
                        {act.domain.toUpperCase()}
                      </span>
                      <span className="text-xs text-slate-400">⏱️ {act.duration_mins} mins</span>
                    </div>
                    <h4 className="font-bold text-white text-base mb-1.5">{act.title}</h4>
                    <p className="text-xs text-slate-400 leading-relaxed mb-4">{act.tagline}</p>
                  </div>

                  <button
                    onClick={() => setActiveExpModal(act)}
                    className="w-full py-2.5 px-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold flex items-center justify-center gap-1.5 transition-all shadow-md shadow-indigo-600/20"
                  >
                    <span>Try Experiment & Give Feedback</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              ))}
            </div>
          </div>

          {/* Master Course Explorer with Category Filters */}
          <div id="all-courses">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-6">
              <div>
                <h3 className="text-xl sm:text-2xl font-bold text-white">
                  Master Roadmap Library
                </h3>
                <p className="text-xs sm:text-sm text-slate-400">
                  Explore all 49 complete roadmaps across disciplines
                </p>
              </div>

              {/* Search Bar */}
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
                    <h4 className="font-extrabold text-white text-lg mb-1.5">
                      {rm.title}
                    </h4>
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
                        setActiveTab("journey");
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
      )}

      {/* Practical Exploration Activity Modal */}
      {activeExpModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-md p-4">
          <div className="bg-slate-900 border border-slate-800 rounded-3xl max-w-xl w-full p-6 sm:p-8 shadow-2xl animate-scale-in">
            <div className="flex items-center justify-between pb-4 border-b border-slate-800 mb-4">
              <div>
                <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md bg-indigo-500/20 text-indigo-300">
                  {activeExpModal.domain.toUpperCase()} Experiment
                </span>
                <h3 className="text-lg font-bold text-white mt-1">{activeExpModal.title}</h3>
              </div>
              <button
                onClick={() => setActiveExpModal(null)}
                className="text-slate-400 hover:text-white text-lg font-bold"
              >
                ✕
              </button>
            </div>

            <p className="text-xs text-slate-300 leading-relaxed mb-4 whitespace-pre-line">
              {activeExpModal.instructions}
            </p>

            {/* Quick Code Example */}
            <div className="p-3 rounded-xl bg-slate-950 border border-slate-800 text-[11px] font-mono text-emerald-300 mb-6 max-h-32 overflow-y-auto">
              <pre>{activeExpModal.starter_code}</pre>
            </div>

            {/* Feedback Questions */}
            <div className="space-y-4 pt-4 border-t border-slate-800">
              <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400">
                Empirical Evidence Reflection:
              </h4>

              {/* Interest rating */}
              <div>
                <label className="text-xs text-slate-300 block mb-1">
                  How exciting did this activity feel? (1 = Boring, 5 = Captivating)
                </label>
                <div className="flex gap-2">
                  {[1, 2, 3, 4, 5].map((val) => (
                    <button
                      key={val}
                      onClick={() => setExpInterest(val)}
                      className={`flex-1 py-1.5 rounded-lg text-xs font-bold border transition-all ${
                        expInterest === val ? "bg-indigo-600 text-white border-indigo-500" : "bg-slate-950 text-slate-400 border-slate-800"
                      }`}
                    >
                      {val}★
                    </button>
                  ))}
                </div>
              </div>

              {/* Would explore further */}
              <div className="flex items-center justify-between text-xs text-slate-300">
                <span>Would you like to explore this domain further?</span>
                <div className="flex gap-2">
                  <button
                    onClick={() => setExpWouldExplore(true)}
                    className={`px-3 py-1 rounded-lg font-bold border ${expWouldExplore ? "bg-emerald-600 text-white border-emerald-500" : "bg-slate-950 text-slate-400 border-slate-800"}`}
                  >
                    Yes
                  </button>
                  <button
                    onClick={() => setExpWouldExplore(false)}
                    className={`px-3 py-1 rounded-lg font-bold border ${!expWouldExplore ? "bg-rose-600 text-white border-rose-500" : "bg-slate-950 text-slate-400 border-slate-800"}`}
                  >
                    No
                  </button>
                </div>
              </div>

              {/* Reflection comments */}
              <div>
                <label className="text-xs text-slate-300 block mb-1">
                  What part did you enjoy or find confusing? (Optional)
                </label>
                <input
                  type="text"
                  placeholder="e.g. Loved reactive state, syntax was clear..."
                  value={expFeedbackText}
                  onChange={(e) => setExpFeedbackText(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl bg-slate-950 border border-slate-800 text-xs text-white placeholder-slate-500 outline-none focus:border-indigo-500"
                />
              </div>

              <button
                onClick={handleSubmitExploration}
                disabled={submittingFeedback}
                className="w-full py-3 rounded-xl bg-gradient-to-r from-indigo-600 to-teal-500 hover:from-indigo-500 hover:to-teal-400 text-white font-bold text-xs sm:text-sm flex items-center justify-center gap-2 transition-all shadow-lg shadow-indigo-600/30"
              >
                {submittingFeedback ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
                <span>{feedbackSuccess ? "Evidence Recorded!" : "Submit & Update Career Ranking"}</span>
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
};
