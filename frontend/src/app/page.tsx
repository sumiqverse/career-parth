"use client";

import React, { useState, useEffect } from "react";
import { Navbar } from "@/components/Navbar";
import { LandingHero } from "@/components/LandingHero";
import { AssessmentWizard } from "@/components/AssessmentWizard";
import { DashboardView } from "@/components/DashboardView";
import { TopicWorkspace } from "@/components/TopicWorkspace";
import { AuthModal } from "@/components/AuthModal";
import { api, authStorage, UserProfile } from "@/lib/api";

export default function Home() {
  const [currentView, setCurrentView] = useState<"landing" | "assessment" | "dashboard" | "workspace" | "courses">("landing");
  const [user, setUser] = useState<UserProfile | null>(null);
  
  // Auth Modal State
  const [authModalOpen, setAuthModalOpen] = useState(false);
  const [authMode, setAuthMode] = useState<"login" | "register">("register");

  // Selected Topic in Workspace
  const [activeRoadmapSlug, setActiveRoadmapSlug] = useState<string>("full-stack-developer");
  const [activeTopicId, setActiveTopicId] = useState<string>("fs_topic_html_css");

  // Load User profile on mount
  useEffect(() => {
    const initUser = async () => {
      const cached = authStorage.getUser();
      if (cached) setUser(cached);
      try {
        const liveUser = await api.getMe();
        if (liveUser) setUser(liveUser);
      } catch (e) {
        console.warn("Could not sync live user profile:", e);
      }
    };
    initUser();
  }, []);

  const handleOpenAuth = (mode: "login" | "register") => {
    setAuthMode(mode);
    setAuthModalOpen(true);
  };

  const handleLogout = () => {
    authStorage.removeToken();
    setUser(null);
    setCurrentView("landing");
  };

  const handleAssessmentComplete = (result: any) => {
    // If user has result, redirect directly to personalized dashboard
    setCurrentView("dashboard");
    // Refresh user profile if logged in
    api.getMe().then((u) => u && setUser(u));
  };

  const handleSelectTopic = (roadmapSlug: string, topicId: string) => {
    setActiveRoadmapSlug(roadmapSlug);
    setActiveTopicId(topicId);
    setCurrentView("workspace");
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleRefreshUser = async () => {
    const liveUser = await api.getMe();
    if (liveUser) setUser(liveUser);
  };

  return (
    <div className="min-h-screen bg-[#090D16] text-slate-100 flex flex-col justify-between selection:bg-indigo-500 selection:text-white">
      
      {/* Global Navigation Bar */}
      <Navbar
        user={user}
        currentView={currentView}
        onOpenAuth={handleOpenAuth}
        onLogout={handleLogout}
        onNavigate={(view) => {
          if (view === "courses") {
            setCurrentView("dashboard");
            setTimeout(() => {
              const el = document.getElementById("all-courses");
              if (el) el.scrollIntoView({ behavior: "smooth" });
            }, 100);
          } else {
            setCurrentView(view);
          }
        }}
      />

      {/* Main Content Router */}
      <main className="flex-1">
        {currentView === "landing" && (
          <LandingHero
            isLoggedIn={!!user}
            onStartAssessment={() => {
              if (!user) {
                // Prompt sign up or let them proceed directly to assessment
                setCurrentView("assessment");
              } else {
                setCurrentView("assessment");
              }
            }}
            onExploreRoadmaps={() => {
              setCurrentView("dashboard");
            }}
            onOpenAuth={() => handleOpenAuth("register")}
          />
        )}

        {currentView === "assessment" && (
          <AssessmentWizard
            onAssessmentComplete={handleAssessmentComplete}
            onCancel={() => setCurrentView("landing")}
          />
        )}

        {currentView === "dashboard" && (
          <DashboardView
            user={user}
            onSelectTopic={handleSelectTopic}
            onStartAssessment={() => setCurrentView("assessment")}
          />
        )}

        {currentView === "workspace" && (
          <TopicWorkspace
            roadmapSlug={activeRoadmapSlug}
            topicId={activeTopicId}
            user={user}
            onBack={() => setCurrentView("dashboard")}
            onRefreshUser={handleRefreshUser}
          />
        )}
      </main>

      {/* Auth Modal */}
      <AuthModal
        isOpen={authModalOpen}
        initialMode={authMode}
        onClose={() => setAuthModalOpen(false)}
        onSuccess={(newUser) => {
          setUser(newUser);
          if (!newUser.primary_domain) {
            setCurrentView("assessment");
          } else {
            setCurrentView("dashboard");
          }
        }}
      />

      {/* Footer */}
      <footer className="border-t border-slate-800/80 bg-slate-950/70 py-8 px-4 text-center">
        <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500">
          <div className="flex items-center gap-2">
            <span className="font-bold text-slate-400">HORIZON AI</span>
            <span>•</span>
            <span>The Unified Learning Experience</span>
          </div>
          <div>
            Empowering self-directed learners with adaptive roadmaps, practical labs, and instant feedback.
          </div>
          <div>
            MongoDB & FastAPI Cloud Persistence
          </div>
        </div>
      </footer>

    </div>
  );
}
