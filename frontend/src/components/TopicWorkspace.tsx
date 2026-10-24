"use client";

import React, { useState, useEffect } from "react";
import { api, TopicDetailPayload, UserProfile } from "@/lib/api";
import { 
  Play, BookOpen, HelpCircle, Code2, Wrench, CheckCircle2, 
  ArrowLeft, Sparkles, Terminal, Check, Copy, Flame, Trophy, Loader2 
} from "lucide-react";
import confetti from "canvas-confetti";

interface TopicWorkspaceProps {
  roadmapSlug: string;
  topicId: string;
  user: UserProfile | null;
  onBack: () => void;
  onRefreshUser: () => void;
}

export const TopicWorkspace: React.FC<TopicWorkspaceProps> = ({
  roadmapSlug,
  topicId,
  user,
  onBack,
  onRefreshUser
}) => {
  const [topicData, setTopicData] = useState<TopicDetailPayload | null>(null);
  const [activeTab, setActiveTab] = useState<"lectures" | "notes" | "questions" | "lab" | "workshop">("lectures");
  const [loading, setLoading] = useState(true);
  
  // Progress states
  const [completedItems, setCompletedItems] = useState<string[]>([]);
  
  // Quiz state
  const [selectedQuizOption, setSelectedQuizOption] = useState<number | null>(null);
  const [quizSubmitted, setQuizSubmitted] = useState(false);

  // Lab code editor state
  const [code, setCode] = useState("");
  const [labRunning, setLabRunning] = useState(false);
  const [labResults, setLabResults] = useState<any | null>(null);

  // Video switcher state
  const [selectedLectureId, setSelectedLectureId] = useState<string | null>(null);
  const [switchingVideo, setSwitchingVideo] = useState(false);

  // Workshop checklist state
  const [checkedSteps, setCheckedSteps] = useState<Record<number, boolean>>({});


  // Adaptive In-Learning Checkpoint State
  const [checkpoint, setCheckpoint] = useState<any | null>(null);
  const [checkpointSubmitted, setCheckpointSubmitted] = useState(false);
  const [checkpointFeedback, setCheckpointFeedback] = useState<string | null>(null);

  useEffect(() => {
    const loadTopic = async () => {
      try {
        setLoading(true);
        const [res, chkRes] = await Promise.all([
          api.getTopicDetails(topicId),
          api.getAdaptiveCheckpoint(topicId)
        ]);
        setTopicData(res.topic);
        if (chkRes && chkRes.available) {
          setCheckpoint(chkRes.checkpoint);
        }
        if (res.user_progress && res.user_progress.completed_items) {
          setCompletedItems(res.user_progress.completed_items);
        }
        if (res.topic && res.topic.lab) {
          setCode(res.topic.lab.starter_code);
        }
      } catch (e) {
        console.error("Failed to load topic details:", e);
      } finally {
        setLoading(false);
      }
    };
    loadTopic();
  }, [topicId]);

  const handleAnswerCheckpoint = async (option: any) => {
    if (!checkpoint) return;
    try {
      const res = await api.submitAdaptiveReflection(
        checkpoint.id,
        topicId,
        option.id,
        option.reinforce_domain
      );
      setCheckpointSubmitted(true);
      setCheckpointFeedback(res.message);
      confetti({ particleCount: 50, spread: 60, origin: { y: 0.5 } });
      onRefreshUser();
    } catch (e) {
      setCheckpointSubmitted(true);
      setCheckpointFeedback("Reflection saved! Calibrating your roadmap.");
    }
  };

  const handleSwitchVideo = async (lectureId: string) => {
    setSelectedLectureId(lectureId);
    setSwitchingVideo(true);
    setTimeout(() => setSwitchingVideo(false), 250);
    try {
      await api.selectTopicVideo(topicId, lectureId);
    } catch (e) {
      console.warn("Could not persist video preference:", e);
    }
  };

  const markActionCompleted = async (actionType: string) => {
    if (completedItems.includes(actionType)) return;

    try {
      const res = await api.completeProgress(roadmapSlug, topicId, actionType);
      setCompletedItems(res.completed_items);
      onRefreshUser();

      // Confetti burst for dopamine reward
      confetti({
        particleCount: 50,
        spread: 60,
        origin: { y: 0.7 }
      });
    } catch (e) {
      console.warn("Failed to persist progress:", e);
      setCompletedItems((prev) => [...prev, actionType]);
    }
  };

  const handleRunLab = async () => {
    if (!topicData?.lab) return;
    setLabRunning(true);
    try {
      const res = await api.runLabCode(code, topicData.lab.test_cases);
      setLabResults(res);
      if (res.success) {
        markActionCompleted("lab");
      }
    } catch (e) {
      console.error("Lab execution error:", e);
    } finally {
      setLabRunning(false);
    }
  };

  if (loading || !topicData) {
    return (
      <div className="max-w-4xl mx-auto py-24 text-center">
        <Loader2 className="w-10 h-10 text-indigo-400 animate-spin mx-auto mb-4" />
        <h3 className="text-xl font-bold text-white mb-1">Loading Learning Workspace...</h3>
        <p className="text-sm text-slate-400">Fetching lectures, notes, quizzes, labs, and workshops</p>
      </div>
    );
  }

  const lecture = (topicData.lectures && topicData.lectures.length > 0)
    ? (topicData.lectures.find((l) => l.id === selectedLectureId) || topicData.recommended_lecture || topicData.lectures[0])
    : null;
  const question = topicData.questions[0] || null;
  const isLectureDone = completedItems.includes("lecture");
  const isNotesDone = completedItems.includes("note");
  const isQuizDone = completedItems.includes("quiz");
  const isLabDone = completedItems.includes("lab");
  const isWorkshopDone = completedItems.includes("workshop");

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 animate-fade-in">
      
      {/* Top Header & Breadcrumb */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800 mb-6">
        <div>
          <button
            onClick={onBack}
            className="inline-flex items-center gap-1.5 text-xs font-semibold text-slate-400 hover:text-white transition-colors mb-2"
          >
            <ArrowLeft className="w-4 h-4" />
            Back to Roadmaps
          </button>
          <div className="flex items-center gap-2 mb-1">
            <span className="text-xs font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2.5 py-0.5 rounded-full border border-indigo-500/20">
              {roadmapSlug.replace(/-/g, " ").toUpperCase()}
            </span>
            <span className="text-xs text-slate-400">• Interactive Masterclass & Lab</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-white">
            {topicData.title}
          </h1>
        </div>

        {/* Progress Tracker Status */}
        <div className="flex items-center gap-3 bg-slate-900 px-4 py-2 rounded-2xl border border-slate-800 self-start sm:self-auto">
          <div className="text-right">
            <span className="text-[11px] text-slate-400 block font-medium">Topic Progress</span>
            <span className="text-xs font-bold text-emerald-400">
              {completedItems.length} of 5 Completed
            </span>
          </div>
          <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
            <Trophy className="w-5 h-5" />
          </div>
        </div>
      </div>

      {/* ADAPTIVE IN-LEARNING PSYCHOLOGICAL CHECKPOINT */}
      {checkpoint && (
        <div className="mb-8 p-5 sm:p-6 rounded-3xl bg-gradient-to-r from-indigo-950/70 via-purple-950/40 to-slate-900 border border-indigo-500/40 shadow-xl relative overflow-hidden">
          <div className="flex items-center gap-2 mb-2 text-xs font-bold uppercase tracking-wider text-cyan-400">
            <Sparkles className="w-4 h-4 text-cyan-300 animate-pulse" />
            <span>Adaptive Career Compass • In-Learning Reflection (+25 XP)</span>
          </div>
          <h3 className="text-base sm:text-lg font-bold text-white mb-3">
            {checkpoint.prompt}
          </h3>
          {!checkpointSubmitted ? (
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
              {checkpoint.options.map((opt: any) => (
                <button
                  key={opt.id}
                  onClick={() => handleAnswerCheckpoint(opt)}
                  className="p-3.5 text-left rounded-2xl bg-slate-950/80 border border-slate-800 hover:border-indigo-400 hover:bg-slate-900 text-xs sm:text-sm text-slate-200 font-medium transition-all transform hover:-translate-y-0.5 shadow-sm"
                >
                  {opt.text}
                </button>
              ))}
            </div>
          ) : (
            <div className="flex items-center gap-2.5 text-xs sm:text-sm font-semibold text-emerald-300 bg-emerald-950/40 p-3.5 rounded-2xl border border-emerald-500/40">
              <CheckCircle2 className="w-5 h-5 text-emerald-400 flex-shrink-0" />
              <span>{checkpointFeedback || "Reflection recorded! Your career roadmap has been dynamically calibrated."}</span>
            </div>
          )}
        </div>
      )}

      {/* 5 LEARNING MODE TABS */}
      <div className="flex overflow-x-auto gap-2 p-1.5 rounded-2xl bg-slate-900 border border-slate-800 mb-8 scrollbar-none">
        
        <button
          onClick={() => setActiveTab("lectures")}
          className={`flex-1 min-w-[130px] py-2.5 px-3 rounded-xl text-xs sm:text-sm font-bold flex items-center justify-center gap-2 transition-all ${
            activeTab === "lectures"
              ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/30"
              : "text-slate-400 hover:text-slate-200"
          }`}
        >
          <Play className="w-4 h-4" />
          <span>1. Lecture</span>
          {isLectureDone && <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />}
        </button>

        <button
          onClick={() => setActiveTab("notes")}
          className={`flex-1 min-w-[130px] py-2.5 px-3 rounded-xl text-xs sm:text-sm font-bold flex items-center justify-center gap-2 transition-all ${
            activeTab === "notes"
              ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/30"
              : "text-slate-400 hover:text-slate-200"
          }`}
        >
          <BookOpen className="w-4 h-4" />
          <span>2. Notes</span>
          {isNotesDone && <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />}
        </button>

        <button
          onClick={() => setActiveTab("questions")}
          className={`flex-1 min-w-[130px] py-2.5 px-3 rounded-xl text-xs sm:text-sm font-bold flex items-center justify-center gap-2 transition-all ${
            activeTab === "questions"
              ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/30"
              : "text-slate-400 hover:text-slate-200"
          }`}
        >
          <HelpCircle className="w-4 h-4" />
          <span>3. Quiz</span>
          {isQuizDone && <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />}
        </button>

        <button
          onClick={() => setActiveTab("lab")}
          className={`flex-1 min-w-[130px] py-2.5 px-3 rounded-xl text-xs sm:text-sm font-bold flex items-center justify-center gap-2 transition-all ${
            activeTab === "lab"
              ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/30"
              : "text-slate-400 hover:text-slate-200"
          }`}
        >
          <Code2 className="w-4 h-4" />
          <span>4. Code Lab</span>
          {isLabDone && <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />}
        </button>

        <button
          onClick={() => setActiveTab("workshop")}
          className={`flex-1 min-w-[130px] py-2.5 px-3 rounded-xl text-xs sm:text-sm font-bold flex items-center justify-center gap-2 transition-all ${
            activeTab === "workshop"
              ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/30"
              : "text-slate-400 hover:text-slate-200"
          }`}
        >
          <Wrench className="w-4 h-4" />
          <span>5. Workshop</span>
          {isWorkshopDone && <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />}
        </button>

      </div>

      {/* TAB 1: LECTURES VIEW (PERSONALIZED GOAT EXPERIENCE) */}
      {activeTab === "lectures" && lecture && (
        <div className="space-y-6">
          {/* Personalized Match Banner */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 p-4 rounded-2xl bg-indigo-950/40 border border-indigo-500/30 shadow-lg shadow-indigo-500/5">
            <div className="flex items-center gap-3">
              <div className="p-2.5 rounded-xl bg-indigo-600/20 border border-indigo-500/40 text-indigo-400 flex-shrink-0">
                <Sparkles className="w-5 h-5 text-indigo-300" />
              </div>
              <div>
                <div className="flex flex-wrap items-center gap-2">
                  <span className="text-xs font-bold text-indigo-300 uppercase tracking-wider">
                    🎯 AI Personalized GOAT Recommendation
                  </span>
                  {lecture.rating && (
                    <span className="text-[11px] font-bold text-amber-300 bg-amber-500/10 px-2 py-0.5 rounded-md border border-amber-500/20">
                      ★ {lecture.rating}
                    </span>
                  )}
                  {lecture.view_count && (
                    <span className="text-[11px] text-slate-400 hidden md:inline">
                      {lecture.view_count}
                    </span>
                  )}
                </div>
                <p className="text-xs text-slate-300 mt-0.5">
                  {lecture.match_reason || topicData.match_reason || "Curated greatest-of-all-time video masterclass for this topic."}
                </p>
              </div>
            </div>

            {/* Quick language/creator indicator */}
            <div className="flex items-center gap-2 flex-shrink-0">
              <span className="text-[11px] font-medium px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-800 text-slate-300">
                {lecture.creator_type === "hinglish_goat" ? "🇮🇳 Hinglish Masterclass" : "🌐 Global GOAT Creator"}
              </span>
            </div>
          </div>

          {/* Interactive Multi-Option Video Switcher Toolbar */}
          {topicData.lectures && topicData.lectures.length > 1 && (
            <div>
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
                  Switch Reference Video (Personalized Options):
                </span>
                <span className="text-[11px] text-indigo-400">
                  Selection auto-saves to your profile
                </span>
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                {topicData.lectures.map((l) => {
                  const isSelected = l.id === lecture.id;
                  return (
                    <button
                      key={l.id}
                      onClick={() => handleSwitchVideo(l.id)}
                      className={`p-3 rounded-2xl border text-left transition-all flex flex-col justify-between ${
                        isSelected
                          ? "bg-slate-900 border-indigo-500 shadow-md shadow-indigo-500/20 ring-1 ring-indigo-500/50"
                          : "bg-slate-950/60 border-slate-800 hover:border-slate-700 hover:bg-slate-900/50 text-slate-400"
                      }`}
                    >
                      <div className="flex items-center justify-between gap-2 mb-1.5">
                        <span className={`text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md ${
                          isSelected ? "bg-indigo-600 text-white" : "bg-slate-800 text-slate-400"
                        }`}>
                          {l.creator_type === "hinglish_goat" ? "🇮🇳 Hinglish" : l.style === "fastpaced_visual" ? "⚡ Fast-Paced" : "📚 Masterclass"}
                        </span>
                        {l.rating && (
                          <span className="text-[11px] text-amber-300 font-semibold">
                            ★ {l.rating}
                          </span>
                        )}
                      </div>
                      <div className="font-bold text-white text-xs line-clamp-1 mb-1">
                        {l.provider}
                      </div>
                      <div className="text-[11px] text-slate-400 line-clamp-1">
                        {l.title}
                      </div>
                    </button>
                  );
                })}
              </div>
            </div>
          )}

          {/* Video Container with smooth fade */}
          <div className={`relative aspect-video w-full rounded-3xl overflow-hidden bg-slate-950 border border-slate-800 shadow-2xl transition-opacity duration-300 ${
            switchingVideo ? "opacity-30" : "opacity-100"
          }`}>
            <iframe
              src={lecture.video_url}
              title={lecture.title}
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
              className="w-full h-full border-0"
            />
          </div>

          {/* Lecture Metadata & Takeaways */}
          <div className="p-6 sm:p-8 rounded-3xl bg-slate-900/80 border border-slate-800">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4 pb-4 border-b border-slate-800">
              <div>
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xs font-semibold text-emerald-400 bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20">
                    Creator: {lecture.provider}
                  </span>
                  <span className="text-xs text-slate-400">
                    ⏱️ {lecture.duration}
                  </span>
                </div>
                <h3 className="text-xl font-bold text-white mt-1">
                  {lecture.title}
                </h3>
              </div>
              <button
                onClick={() => markActionCompleted("lecture")}
                disabled={isLectureDone}
                className={`px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition-all ${
                  isLectureDone
                    ? "bg-emerald-600/20 text-emerald-400 border border-emerald-500/30"
                    : "bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-600/30"
                }`}
              >
                <CheckCircle2 className="w-4 h-4" />
                <span>{isLectureDone ? "Lecture Completed (+25 XP)" : "Mark as Watched (+25 XP)"}</span>
              </button>
            </div>

            <p className="text-sm text-slate-300 leading-relaxed mb-6">
              {lecture.summary}
            </p>

            <h4 className="font-bold text-white text-sm mb-3">Key Architectural Takeaways:</h4>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              {lecture.key_takeaways.map((point, idx) => (
                <div key={idx} className="flex items-start gap-2.5 p-3 rounded-xl bg-slate-950/70 border border-slate-800/80 text-xs text-slate-300">
                  <Check className="w-4 h-4 text-emerald-400 flex-shrink-0 mt-0.5" />
                  <span>{point}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: NOTES VIEW */}
      {activeTab === "notes" && (
        <div className="p-6 sm:p-10 rounded-3xl bg-slate-900/80 border border-slate-800 shadow-2xl">
          <div className="flex items-center justify-between pb-6 border-b border-slate-800 mb-6">
            <div>
              <span className="text-xs font-bold uppercase tracking-wider text-indigo-400">Theoretical Mastery</span>
              <h2 className="text-xl sm:text-2xl font-bold text-white">Study Notes & Reference</h2>
            </div>
            <button
              onClick={() => markActionCompleted("note")}
              disabled={isNotesDone}
              className={`px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition-all ${
                isNotesDone
                  ? "bg-emerald-600/20 text-emerald-400 border border-emerald-500/30"
                  : "bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-600/30"
              }`}
            >
              <CheckCircle2 className="w-4 h-4" />
              <span>{isNotesDone ? "Notes Read (+20 XP)" : "Mark Notes Read (+20 XP)"}</span>
            </button>
          </div>

          <div className="prose prose-invert max-w-none text-slate-300 leading-relaxed space-y-4">
            <div className="whitespace-pre-line font-mono text-sm bg-slate-950 p-6 rounded-2xl border border-slate-800/80 overflow-x-auto">
              {topicData.notes}
            </div>
          </div>
        </div>
      )}

      {/* TAB 3: QUESTIONS VIEW */}
      {activeTab === "questions" && question && (
        <div className="max-w-2xl mx-auto p-6 sm:p-8 rounded-3xl bg-slate-900/80 border border-slate-800 shadow-2xl">
          <div className="flex items-center justify-between mb-4">
            <span className="text-xs font-bold uppercase tracking-wider text-cyan-400 bg-cyan-500/10 px-2.5 py-0.5 rounded-full border border-cyan-500/20">
              Interactive Knowledge Check
            </span>
            <span className="text-xs font-semibold text-indigo-400">+{question.xp} XP</span>
          </div>

          <h3 className="text-lg sm:text-xl font-bold text-white mb-6">
            {question.question}
          </h3>

          <div className="space-y-3 mb-6">
            {question.options.map((opt, idx) => {
              const isSelected = selectedQuizOption === idx;
              let btnClass = "bg-slate-950/70 border-slate-800 text-slate-300 hover:border-slate-700";
              if (quizSubmitted) {
                if (idx === question.correct_option) {
                  btnClass = "bg-emerald-950/40 border-emerald-500 text-emerald-300 font-semibold";
                } else if (isSelected) {
                  btnClass = "bg-rose-950/40 border-rose-500 text-rose-300";
                }
              } else if (isSelected) {
                btnClass = "bg-indigo-950/60 border-indigo-500 text-white font-semibold";
              }

              return (
                <div
                  key={idx}
                  onClick={() => !quizSubmitted && setSelectedQuizOption(idx)}
                  className={`p-4 rounded-2xl border cursor-pointer transition-all flex items-center justify-between ${btnClass}`}
                >
                  <span className="text-sm font-medium">{opt}</span>
                  {quizSubmitted && idx === question.correct_option && (
                    <CheckCircle2 className="w-5 h-5 text-emerald-400" />
                  )}
                </div>
              );
            })}
          </div>

          {!quizSubmitted ? (
            <button
              onClick={() => {
                if (selectedQuizOption === null) return;
                setQuizSubmitted(true);
                if (selectedQuizOption === question.correct_option) {
                  markActionCompleted("quiz");
                }
              }}
              disabled={selectedQuizOption === null}
              className="w-full py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm shadow-lg shadow-indigo-600/30 transition-all disabled:opacity-40"
            >
              Verify Answer
            </button>
          ) : (
            <div className="p-4 rounded-2xl bg-slate-950 border border-slate-800">
              <h5 className="font-bold text-sm text-white mb-1">
                {selectedQuizOption === question.correct_option
                  ? "✓ Brilliant! That's correct."
                  : "✗ Not quite. Here is why:"}
              </h5>
              <p className="text-xs text-slate-400 leading-relaxed mb-3">
                {question.explanation}
              </p>
              <button
                onClick={() => {
                  setQuizSubmitted(false);
                  setSelectedQuizOption(null);
                }}
                className="text-xs font-semibold text-indigo-400 hover:underline"
              >
                Try Again
              </button>
            </div>
          )}
        </div>
      )}

      {/* TAB 4: CODE LAB VIEW */}
      {activeTab === "lab" && topicData.lab && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Instructions Column */}
          <div className="p-6 rounded-3xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-2.5 py-0.5 rounded-full border border-indigo-500/20">
                  Interactive Code Challenge
                </span>
                <span className="text-xs font-bold text-amber-400">+{topicData.lab.xp} XP</span>
              </div>
              <h3 className="text-xl font-bold text-white mb-2">
                {topicData.lab.title}
              </h3>
              <p className="text-sm text-slate-300 leading-relaxed mb-4">
                {topicData.lab.instructions}
              </p>

              <div className="p-4 rounded-2xl bg-slate-950 border border-slate-800/80 mb-4">
                <span className="text-xs font-bold text-amber-300 block mb-1">💡 Solution Hint:</span>
                <p className="text-xs text-slate-400 font-mono">
                  {topicData.lab.hint}
                </p>
              </div>
            </div>

            {/* Test Results Console */}
            {labResults && (
              <div className={`p-4 rounded-2xl border ${
                labResults.success
                  ? "bg-emerald-950/30 border-emerald-500/40 text-emerald-300"
                  : "bg-rose-950/30 border-rose-500/40 text-rose-300"
              }`}>
                <div className="flex items-center gap-2 font-bold text-xs mb-2">
                  <Terminal className="w-4 h-4" />
                  <span>{labResults.feedback}</span>
                </div>
                <div className="space-y-1">
                  {labResults.results.map((r: any, i: number) => (
                    <div key={i} className="text-[11px] font-mono flex items-center gap-1.5">
                      <span>{r.passed ? "✓" : "✗"}</span>
                      <span>{r.description}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Interactive Code Editor Column */}
          <div className="p-6 rounded-3xl bg-slate-950 border border-slate-800 flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between pb-3 border-b border-slate-800 mb-3">
                <span className="text-xs font-mono text-slate-400">
                  solution.{topicData.lab.language === "python" ? "py" : topicData.lab.language === "css" ? "css" : "js"}
                </span>
                <span className="text-[11px] text-slate-500 uppercase">
                  {topicData.lab.language}
                </span>
              </div>
              <textarea
                value={code}
                onChange={(e) => setCode(e.target.value)}
                rows={12}
                className="w-full bg-transparent font-mono text-xs sm:text-sm text-indigo-200 outline-none resize-none leading-relaxed"
                placeholder="Write your code here..."
              />
            </div>

            <button
              onClick={handleRunLab}
              disabled={labRunning}
              className="mt-4 w-full py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-sm shadow-lg shadow-emerald-600/30 flex items-center justify-center gap-2 transition-all disabled:opacity-50"
            >
              {labRunning ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>Running Test Cases...</span>
                </>
              ) : (
                <>
                  <Play className="w-4 h-4 fill-white" />
                  <span>Run Code & Verify Tests (+50 XP)</span>
                </>
              )}
            </button>
          </div>
        </div>
      )}

      {/* TAB 5: WORKSHOP VIEW */}
      {activeTab === "workshop" && topicData.workshop && (
        <div className="p-6 sm:p-10 rounded-3xl bg-slate-900/80 border border-slate-800 shadow-2xl">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800 mb-6">
            <div>
              <span className="text-xs font-bold uppercase tracking-wider text-amber-400 bg-amber-500/10 px-2.5 py-0.5 rounded-full border border-amber-500/20">
                Capstone Project Guided Build
              </span>
              <h2 className="text-xl sm:text-2xl font-bold text-white mt-1">
                {topicData.workshop.title}
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 mt-0.5">
                {topicData.workshop.tagline}
              </p>
            </div>
            <button
              onClick={() => markActionCompleted("workshop")}
              disabled={isWorkshopDone}
              className={`px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition-all ${
                isWorkshopDone
                  ? "bg-emerald-600/20 text-emerald-400 border border-emerald-500/30"
                  : "bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-600/30"
              }`}
            >
              <CheckCircle2 className="w-4 h-4" />
              <span>{isWorkshopDone ? "Workshop Done (+100 XP)" : "Complete Milestone (+100 XP)"}</span>
            </button>
          </div>

          <p className="text-sm text-slate-300 leading-relaxed mb-6">
            {topicData.workshop.overview}
          </p>

          <h4 className="font-bold text-white text-sm mb-3">Step-by-Step Implementation Guide:</h4>
          <div className="space-y-3 mb-8">
            {topicData.workshop.steps.map((step, idx) => {
              const isChecked = !!checkedSteps[idx];
              return (
                <div
                  key={idx}
                  onClick={() => setCheckedSteps((prev) => ({ ...prev, [idx]: !prev[idx] }))}
                  className={`p-4 rounded-2xl border cursor-pointer transition-all flex items-center justify-between ${
                    isChecked
                      ? "bg-emerald-950/20 border-emerald-500/40 text-emerald-200"
                      : "bg-slate-950/70 border-slate-800 text-slate-300 hover:border-slate-700"
                  }`}
                >
                  <span className="text-sm font-medium">{step}</span>
                  <div className={`w-5 h-5 rounded-lg border flex items-center justify-center transition-all ${
                    isChecked
                      ? "border-emerald-500 bg-emerald-600 text-white"
                      : "border-slate-700 bg-slate-900"
                  }`}>
                    {isChecked && <Check className="w-3.5 h-3.5" />}
                  </div>
                </div>
              );
            })}
          </div>

          <h4 className="font-bold text-white text-sm mb-3">Acceptance Criteria:</h4>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {topicData.workshop.acceptance_criteria.map((crit, idx) => (
              <div key={idx} className="flex items-center gap-2 text-xs text-slate-400 p-3 rounded-xl bg-slate-950 border border-slate-800/80">
                <Check className="w-3.5 h-3.5 text-indigo-400" />
                <span>{crit}</span>
              </div>
            ))}
          </div>
        </div>
      )}

    </div>
  );
};
