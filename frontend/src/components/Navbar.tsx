"use client";

import React from "react";
import { UserProfile } from "@/lib/api";
import { 
  Compass, Flame, Zap, Trophy, LogIn, UserPlus, LogOut, 
  Sparkles, Layers, BookOpen 
} from "lucide-react";

interface NavbarProps {
  user: UserProfile | null;
  onOpenAuth: (mode: "login" | "register") => void;
  onLogout: () => void;
  onNavigate: (view: "landing" | "assessment" | "dashboard" | "courses") => void;
  currentView: string;
}

export const Navbar: React.FC<NavbarProps> = ({
  user,
  onOpenAuth,
  onLogout,
  onNavigate,
  currentView
}) => {
  return (
    <header className="sticky top-0 z-50 w-full border-b border-slate-800/80 bg-slate-950/80 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        {/* Brand / Logo */}
        <div 
          onClick={() => onNavigate("landing")}
          className="flex items-center gap-2.5 cursor-pointer group"
        >
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 via-indigo-500 to-cyan-400 p-0.5 shadow-lg shadow-indigo-500/25 group-hover:scale-105 transition-transform duration-300">
            <div className="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
              <Compass className="w-5 h-5 text-indigo-400 group-hover:rotate-45 transition-transform duration-500" />
            </div>
          </div>
          <div>
            <div className="flex items-center gap-1.5">
              <span className="font-extrabold text-xl tracking-tight text-white">HORIZON</span>
              <span className="text-[10px] font-semibold uppercase tracking-wider px-1.5 py-0.5 rounded bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                AI Learn
              </span>
            </div>
            <span className="text-[11px] text-slate-400 block -mt-0.5 font-medium">
              Adaptive Paths • Hands-on Labs • Real Mastery
            </span>
          </div>
        </div>

        {/* Navigation Links */}
        <nav className="hidden md:flex items-center gap-1">
          <button
            onClick={() => onNavigate("landing")}
            className={`px-3.5 py-2 text-sm font-medium rounded-lg transition-all ${
              currentView === "landing"
                ? "text-white bg-slate-800/80 shadow-sm"
                : "text-slate-400 hover:text-slate-200 hover:bg-slate-900/60"
            }`}
          >
            Overview
          </button>
          <button
            onClick={() => onNavigate("dashboard")}
            className={`px-3.5 py-2 text-sm font-medium rounded-lg transition-all flex items-center gap-1.5 ${
              currentView === "dashboard"
                ? "text-white bg-slate-800/80 shadow-sm"
                : "text-slate-400 hover:text-slate-200 hover:bg-slate-900/60"
            }`}
          >
            <Layers className="w-4 h-4 text-indigo-400" />
            My Roadmaps
          </button>
          <button
            onClick={() => onNavigate("assessment")}
            className={`px-3.5 py-2 text-sm font-medium rounded-lg transition-all flex items-center gap-1.5 ${
              currentView === "assessment"
                ? "text-indigo-400 bg-indigo-950/40 border border-indigo-500/30"
                : "text-indigo-300/90 hover:text-white hover:bg-indigo-950/30"
            }`}
          >
            <Sparkles className="w-4 h-4 text-cyan-400 animate-pulse" />
            15-Q Diagnostic
          </button>
          <button
            onClick={() => onNavigate("courses")}
            className={`px-3.5 py-2 text-sm font-medium rounded-lg transition-all flex items-center gap-1.5 ${
              currentView === "courses"
                ? "text-white bg-slate-800/80 shadow-sm"
                : "text-slate-400 hover:text-slate-200 hover:bg-slate-900/60"
            }`}
          >
            <BookOpen className="w-4 h-4 text-emerald-400" />
            All Courses
          </button>
        </nav>

        {/* Right Action / Gamification Bar */}
        <div className="flex items-center gap-3">
          {user ? (
            <div className="flex items-center gap-2 sm:gap-3">
              {/* Streak Badge */}
              <div 
                title={`${user.streak} Day Learning Streak`}
                className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-semibold"
              >
                <Flame className="w-3.5 h-3.5 text-amber-400 fill-amber-400 animate-bounce" />
                <span>{user.streak}d</span>
              </div>

              {/* XP Badge */}
              <div 
                title={`${user.xp} Total XP Earned`}
                className="flex items-center gap-1 px-2.5 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 text-xs font-semibold"
              >
                <Zap className="w-3.5 h-3.5 text-indigo-400 fill-indigo-400" />
                <span>{user.xp} XP</span>
              </div>

              {/* Level Pill */}
              <div 
                title={`Level ${user.level}`}
                className="hidden sm:flex items-center gap-1 px-2.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs font-semibold"
              >
                <Trophy className="w-3.5 h-3.5 text-emerald-400" />
                <span>Lvl {user.level}</span>
              </div>

              {/* User Dropdown / Logout */}
              <div className="flex items-center gap-2 pl-1 border-l border-slate-800">
                <span className="text-xs font-medium text-slate-300 hidden md:inline max-w-[120px] truncate">
                  {user.full_name}
                </span>
                <button
                  onClick={onLogout}
                  title="Sign Out"
                  className="p-1.5 rounded-lg text-slate-400 hover:text-rose-400 hover:bg-rose-950/30 transition-colors"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              </div>
            </div>
          ) : (
            <div className="flex items-center gap-2">
              <button
                onClick={() => onOpenAuth("login")}
                className="px-3 py-1.5 text-xs sm:text-sm font-medium text-slate-300 hover:text-white transition-colors"
              >
                Sign In
              </button>
              <button
                onClick={() => onOpenAuth("register")}
                className="px-3.5 py-1.5 text-xs sm:text-sm font-medium rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-600/30 transition-all flex items-center gap-1.5"
              >
                <UserPlus className="w-3.5 h-3.5" />
                Sign Up
              </button>
            </div>
          )}
        </div>

      </div>
    </header>
  );
};
