"use client";

import React from "react";
import { 
  Sparkles, ArrowRight, CheckCircle2, Flame, Layers, 
  Code2, BrainCircuit, ShieldCheck, Terminal, Compass 
} from "lucide-react";

interface LandingHeroProps {
  onStartAssessment: () => void;
  onExploreRoadmaps: () => void;
  onOpenAuth: () => void;
  isLoggedIn: boolean;
}

export const LandingHero: React.FC<LandingHeroProps> = ({
  onStartAssessment,
  onExploreRoadmaps,
  onOpenAuth,
  isLoggedIn
}) => {
  return (
    <div className="relative overflow-hidden pt-12 pb-20">
      
      {/* Background Ambient Glows */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[650px] h-[350px] bg-gradient-to-tr from-indigo-600/20 via-purple-600/15 to-cyan-500/10 blur-[130px] pointer-events-none -z-10" />
      <div className="absolute top-1/3 left-10 w-[300px] h-[300px] bg-indigo-500/10 blur-[100px] pointer-events-none -z-10" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Top Tagline Pill */}
        <div className="flex justify-center mb-6">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-900/90 border border-indigo-500/30 text-indigo-300 text-xs sm:text-sm font-medium shadow-lg shadow-indigo-500/10">
            <Sparkles className="w-4 h-4 text-cyan-400 animate-pulse" />
            <span>The Unified AI Learning Platform</span>
            <span className="w-1.5 h-1.5 rounded-full bg-indigo-400" />
            <span className="text-slate-400 hidden sm:inline">Architected for Zero Overwhelm & Pure Mastery</span>
          </div>
        </div>

        {/* Hero Title */}
        <div className="text-center max-w-4xl mx-auto mb-8">
          <h1 className="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight text-white leading-[1.1] mb-6">
            Master Any Tech Skill.{" "}
            <span className="gradient-text-primary block mt-1">
              Zero Confusion. Zero Overwhelm.
            </span>
          </h1>
          <p className="text-lg sm:text-xl text-slate-300 max-w-2xl mx-auto leading-relaxed">
            Stop drowning in 50-hour tutorial playlists. Horizon unifies structured visual roadmaps, hands-on interactive code labs, and gamified mastery loops into one seamless personalized experience.
          </p>
        </div>

        {/* Primary Action Buttons */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-16">
          <button
            onClick={onStartAssessment}
            className="w-full sm:w-auto px-8 py-4 rounded-xl bg-gradient-to-r from-indigo-600 via-indigo-500 to-cyan-500 hover:from-indigo-500 hover:to-cyan-400 text-white font-bold text-base shadow-xl shadow-indigo-600/30 flex items-center justify-center gap-3 transition-all transform hover:-translate-y-0.5"
          >
            <Sparkles className="w-5 h-5 text-cyan-200" />
            <span>Take 15-Question Diagnostic</span>
            <ArrowRight className="w-4 h-4" />
          </button>
          <button
            onClick={onExploreRoadmaps}
            className="w-full sm:w-auto px-8 py-4 rounded-xl bg-slate-900/80 hover:bg-slate-800/80 border border-slate-700/80 text-slate-200 hover:text-white font-semibold text-base transition-all flex items-center justify-center gap-2"
          >
            <Layers className="w-5 h-5 text-indigo-400" />
            <span>Explore All Roadmaps</span>
          </button>
        </div>

        {/* 3 Unified Web Pillars Bar */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto mb-20">
          
          <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800/80 hover:border-indigo-500/30 transition-all">
            <div className="flex items-center gap-3 mb-3">
              <div className="p-2.5 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400">
                <Compass className="w-5 h-5" />
              </div>
              <div>
                <h3 className="font-bold text-white text-base">Visual Roadmap Engine</h3>
                <span className="text-xs text-indigo-300 font-medium">Clear Milestone Hierarchy</span>
              </div>
            </div>
            <p className="text-sm text-slate-400">
              Clear milestone progression. Understand exactly where you are, what to learn next, and the dependencies between topics.
            </p>
          </div>

          <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800/80 hover:border-emerald-500/30 transition-all">
            <div className="flex items-center gap-3 mb-3">
              <div className="p-2.5 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400">
                <Code2 className="w-5 h-5" />
              </div>
              <div>
                <h3 className="font-bold text-white text-base">Interactive Project Labs</h3>
                <span className="text-xs text-emerald-300 font-medium">Masterclasses & Practical Labs</span>
              </div>
            </div>
            <p className="text-sm text-slate-400">
              Comprehensive curated video walkthroughs, in-browser code editor labs, and real capstone workshops mapped topic-by-topic.
            </p>
          </div>

          <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800/80 hover:border-amber-500/30 transition-all">
            <div className="flex items-center gap-3 mb-3">
              <div className="p-2.5 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400">
                <Flame className="w-5 h-5" />
              </div>
              <div>
                <h3 className="font-bold text-white text-base">Gamified Mastery Loops</h3>
                <span className="text-xs text-amber-300 font-medium">XP, Streaks & Feedback</span>
              </div>
            </div>
            <p className="text-sm text-slate-400">
              Instant dopamine loops: Daily streaks, quiz validation with XP rewards, code test runners, and level progression badges.
            </p>
          </div>

        </div>

        {/* How It Works: 4 Step Ribbon */}
        <div className="max-w-5xl mx-auto rounded-3xl bg-slate-900/40 border border-slate-800/80 p-8 sm:p-10 mb-16">
          <div className="text-center mb-10">
            <span className="text-xs font-bold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-3 py-1 rounded-full border border-indigo-500/20">
              The 4-Step Learning Engine
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold text-white mt-3">
              From "Where do I start?" to Confident Production Code
            </h2>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            
            <div className="relative p-5 rounded-2xl bg-slate-950/60 border border-slate-800">
              <span className="text-3xl font-black text-indigo-500/40 block mb-2">01</span>
              <h4 className="font-bold text-white text-sm mb-1.5">15-Q Diagnostic</h4>
              <p className="text-xs text-slate-400 leading-relaxed">
                Answer 15 smart questions to map your affinity across Full Stack, Backend, AI/ML, DevOps, and Security.
              </p>
            </div>

            <div className="relative p-5 rounded-2xl bg-slate-950/60 border border-slate-800">
              <span className="text-3xl font-black text-cyan-500/40 block mb-2">02</span>
              <h4 className="font-bold text-white text-sm mb-1.5">Top 4 Roadmaps</h4>
              <p className="text-xs text-slate-400 leading-relaxed">
                Receive your Top 4 curated personalized paths ranked specifically for your cognitive style and goals.
              </p>
            </div>

            <div className="relative p-5 rounded-2xl bg-slate-950/60 border border-slate-800">
              <span className="text-3xl font-black text-emerald-500/40 block mb-2">03</span>
              <h4 className="font-bold text-white text-sm mb-1.5">5 Learning Modes</h4>
              <p className="text-xs text-slate-400 leading-relaxed">
                For every topic: watch video lectures, review notes, pass quizzes, solve labs, and complete workshops.
              </p>
            </div>

            <div className="relative p-5 rounded-2xl bg-slate-950/60 border border-slate-800">
              <span className="text-3xl font-black text-amber-500/40 block mb-2">04</span>
              <h4 className="font-bold text-white text-sm mb-1.5">Persistent Progress</h4>
              <p className="text-xs text-slate-400 leading-relaxed">
                Every quiz score, lab solution, and lecture watched is saved to MongoDB. Build daily streaks and earn badges.
              </p>
            </div>

          </div>
        </div>

      </div>
    </div>
  );
};
