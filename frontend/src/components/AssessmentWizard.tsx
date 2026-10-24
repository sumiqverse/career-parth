"use client";

import React, { useState, useEffect } from "react";
import { AssessmentQuestion, api, RoadmapSummary } from "@/lib/api";
import { 
  Sparkles, ArrowRight, ArrowLeft, CheckCircle2, 
  BrainCircuit, Layers, Trophy, Compass, ShieldCheck, Server 
} from "lucide-react";
import confetti from "canvas-confetti";

interface AssessmentWizardProps {
  onAssessmentComplete: (result: {
    recommended_domain: string;
    domain_display_name: string;
    tagline: string;
    description: string;
    top_roadmaps: RoadmapSummary[];
  }) => void;
  onCancel: () => void;
}

export const AssessmentWizard: React.FC<AssessmentWizardProps> = ({
  onAssessmentComplete,
  onCancel
}) => {
  const [questions, setQuestions] = useState<AssessmentQuestion[]>([]);
  const [loading, setLoading] = useState(true);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [analyzing, setAnalyzing] = useState(false);
  const [result, setResult] = useState<any | null>(null);

  useEffect(() => {
    const loadQuestions = async () => {
      try {
        setLoading(true);
        const data = await api.getAssessmentQuestions();
        if (data && data.length > 0) {
          setQuestions(data);
        } else {
          // Fallback questions if backend is temporarily starting
          setQuestions(getFallbackQuestions());
        }
      } catch (e) {
        setQuestions(getFallbackQuestions());
      } finally {
        setLoading(false);
      }
    };
    loadQuestions();
  }, []);

  const handleSelectOption = (optionId: string) => {
    const currentQ = questions[currentIndex];
    const newAnswers = { ...answers, [currentQ.id.toString()]: optionId };
    setAnswers(newAnswers);

    // Auto advance to next question after small tactile delay
    if (currentIndex < questions.length - 1) {
      setTimeout(() => {
        setCurrentIndex((prev) => prev + 1);
      }, 250);
    }
  };

  const handleSubmit = async () => {
    setAnalyzing(true);
    try {
      const res = await api.submitAssessment(answers);
      setResult(res);
      // Trigger celebratory confetti on assessment completion
      confetti({
        particleCount: 80,
        spread: 70,
        origin: { y: 0.6 }
      });
    } catch (e) {
      // Offline fallback calculation
      const fallbackResult = {
        recommended_domain: "fullstack",
        domain_display_name: "Full Stack Web Development",
        tagline: "The Complete Product Builder",
        description: "You thrive when building complete products from end to end. From dynamic frontend components to robust APIs, databases, and deployment pipelines.",
        top_roadmaps: []
      };
      setResult(fallbackResult);
    } finally {
      setAnalyzing(false);
    }
  };

  if (loading) {
    return (
      <div className="max-w-2xl mx-auto py-24 text-center">
        <div className="w-12 h-12 rounded-2xl bg-indigo-600/20 border border-indigo-500/30 flex items-center justify-center mx-auto mb-4 animate-spin">
          <Sparkles className="w-6 h-6 text-indigo-400" />
        </div>
        <h3 className="text-xl font-bold text-white mb-2">Preparing 15 Diagnostic Questions...</h3>
        <p className="text-sm text-slate-400">Loading personalized evaluation criteria</p>
      </div>
    );
  }

  // --- Analyzing State ---
  if (analyzing) {
    return (
      <div className="max-w-xl mx-auto py-24 px-4 text-center">
        <div className="w-20 h-20 rounded-3xl bg-gradient-to-tr from-indigo-600 to-cyan-500 p-1 mx-auto mb-6 animate-pulse shadow-xl shadow-indigo-500/25">
          <div className="w-full h-full bg-slate-950 rounded-[22px] flex items-center justify-center">
            <BrainCircuit className="w-10 h-10 text-cyan-400 animate-spin" />
          </div>
        </div>
        <h2 className="text-2xl sm:text-3xl font-extrabold text-white mb-3">
          Synthesizing Your Engineering DNA...
        </h2>
        <p className="text-slate-400 text-sm max-w-md mx-auto mb-6">
          Analyzing your responses across algorithmic thinking, visual layout preference, systems affinity, and career goals.
        </p>
        <div className="w-full max-w-xs mx-auto bg-slate-800 rounded-full h-2 overflow-hidden">
          <div className="bg-gradient-to-r from-indigo-500 to-cyan-400 h-full animate-[progress_1.5s_ease-in-out_infinite]" style={{ width: "80%" }} />
        </div>
      </div>
    );
  }

  // --- Results View ---
  if (result) {
    return (
      <div className="max-w-3xl mx-auto py-12 px-4 animate-fade-in">
        <div className="text-center mb-8">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs font-semibold mb-3">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            Diagnosis Complete • 100 XP Awarded
          </div>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
            Your Optimal Engineering Path
          </h2>
          <p className="text-slate-400 text-sm mt-1">
            Based on your 15 responses, here is where your technical potential will accelerate fastest:
          </p>
        </div>

        {/* Recommended Domain Highlight Card */}
        <div className="p-8 rounded-3xl bg-gradient-to-b from-indigo-950/60 to-slate-900/90 border border-indigo-500/40 shadow-2xl shadow-indigo-950/50 mb-8 relative overflow-hidden">
          <div className="absolute top-0 right-0 w-64 h-64 bg-indigo-500/10 rounded-full blur-3xl -z-10" />
          
          <div className="flex items-center gap-3 mb-4">
            <div className="p-3 rounded-2xl bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
              <Compass className="w-7 h-7" />
            </div>
            <div>
              <span className="text-xs font-bold uppercase tracking-wider text-indigo-400">Primary Recommendation</span>
              <h3 className="text-2xl sm:text-3xl font-extrabold text-white">
                {result.domain_display_name}
              </h3>
            </div>
          </div>

          <p className="text-base text-indigo-200/90 font-medium italic mb-4">
            "{result.tagline}"
          </p>
          <p className="text-sm text-slate-300 leading-relaxed mb-6">
            {result.description}
          </p>

          <button
            onClick={() => onAssessmentComplete(result)}
            className="w-full sm:w-auto px-8 py-3.5 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-500 hover:from-indigo-500 hover:to-cyan-400 text-white font-bold text-sm shadow-xl shadow-indigo-600/30 flex items-center justify-center gap-2 transition-all transform hover:-translate-y-0.5"
          >
            <span>Proceed to Top 4 Roadmaps</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    );
  }

  // --- Question Card View ---
  const currentQuestion = questions[currentIndex];
  const progressPercent = Math.round(((currentIndex + 1) / questions.length) * 100);
  const selectedOptionId = currentQuestion ? answers[currentQuestion.id.toString()] : null;
  const isLastQuestion = currentIndex === questions.length - 1;
  const allAnswered = Object.keys(answers).length >= questions.length;

  return (
    <div className="max-w-3xl mx-auto py-10 px-4">
      
      {/* Top Header & Progress */}
      <div className="flex items-center justify-between mb-3 text-xs font-medium text-slate-400">
        <button
          onClick={onCancel}
          className="hover:text-slate-200 transition-colors"
        >
          ← Exit Diagnostic
        </button>
        <span className="font-semibold text-indigo-400">
          Question {currentIndex + 1} of {questions.length} ({progressPercent}%)
        </span>
      </div>

      {/* Progress Bar */}
      <div className="w-full bg-slate-900 rounded-full h-2 mb-8 border border-slate-800 overflow-hidden">
        <div 
          className="bg-gradient-to-r from-indigo-500 via-indigo-400 to-cyan-400 h-full rounded-full transition-all duration-300"
          style={{ width: `${progressPercent}%` }}
        />
      </div>

      {/* Question Header Card */}
      <div className="p-6 sm:p-8 rounded-3xl bg-slate-900/80 border border-slate-800 shadow-xl mb-6">
        <div className="inline-block px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-300 text-xs font-semibold mb-3">
          Category: {currentQuestion.category}
        </div>
        <h2 className="text-xl sm:text-2xl font-bold text-white leading-snug">
          {currentQuestion.question}
        </h2>
      </div>

      {/* Options List */}
      <div className="space-y-3 mb-8">
        {currentQuestion.options.map((option, idx) => {
          const isSelected = selectedOptionId === option.id;
          return (
            <div
              key={option.id}
              onClick={() => handleSelectOption(option.id)}
              className={`p-4 sm:p-5 rounded-2xl border cursor-pointer transition-all flex items-center justify-between ${
                isSelected
                  ? "bg-indigo-950/60 border-indigo-500/70 shadow-lg shadow-indigo-950/50"
                  : "bg-slate-900/50 border-slate-800 hover:border-slate-700 hover:bg-slate-900/80"
              }`}
            >
              <div className="flex items-center gap-3.5">
                <div className={`w-8 h-8 rounded-xl flex items-center justify-center text-xs font-bold transition-colors ${
                  isSelected
                    ? "bg-indigo-600 text-white"
                    : "bg-slate-800 text-slate-400"
                }`}>
                  {String.fromCharCode(65 + idx)}
                </div>
                <span className={`text-sm sm:text-base font-medium ${
                  isSelected ? "text-white font-semibold" : "text-slate-300"
                }`}>
                  {option.text}
                </span>
              </div>

              <div className={`w-5 h-5 rounded-full border flex items-center justify-center transition-all ${
                isSelected
                  ? "border-indigo-400 bg-indigo-500 text-white"
                  : "border-slate-700 bg-slate-950"
              }`}>
                {isSelected && <CheckCircle2 className="w-4 h-4 fill-white text-indigo-600" />}
              </div>
            </div>
          );
        })}
      </div>

      {/* Footer Navigation */}
      <div className="flex items-center justify-between pt-4 border-t border-slate-800/80">
        <button
          onClick={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
          disabled={currentIndex === 0}
          className="px-4 py-2 text-sm font-medium rounded-xl text-slate-400 hover:text-white disabled:opacity-30 disabled:pointer-events-none flex items-center gap-1.5 transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          Previous
        </button>

        {isLastQuestion ? (
          <button
            onClick={handleSubmit}
            disabled={!selectedOptionId}
            className="px-6 py-2.5 rounded-xl bg-gradient-to-r from-indigo-600 to-cyan-500 hover:from-indigo-500 hover:to-cyan-400 text-white text-sm font-bold shadow-lg shadow-indigo-600/30 flex items-center gap-2 transition-all disabled:opacity-40"
          >
            <Sparkles className="w-4 h-4 text-cyan-200" />
            <span>Generate Recommended Path</span>
          </button>
        ) : (
          <button
            onClick={() => setCurrentIndex((prev) => Math.min(questions.length - 1, prev + 1))}
            disabled={!selectedOptionId}
            className="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold flex items-center gap-1.5 transition-all disabled:opacity-30"
          >
            <span>Next</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        )}
      </div>

    </div>
  );
};

// Fallback questions if backend is temporarily offline
function getFallbackQuestions(): AssessmentQuestion[] {
  return [
    {
      id: 1,
      category: "Interests",
      question: "When working on a digital project, which part excites you the most?",
      options: [
        { id: "q1_a", text: "Designing sleek, responsive user interfaces with smooth animations", domain_scores: { frontend: 4 } },
        { id: "q1_b", text: "Architecting database schemas, business logic, and fast APIs", domain_scores: { backend: 4 } },
        { id: "q1_c", text: "Training smart models that can recognize patterns or generate insights", domain_scores: { ai_ml: 4 } },
        { id: "q1_d", text: "Automating cloud deployments, servers, and zero-downtime infrastructure", domain_scores: { devops: 4 } }
      ]
    },
    {
      id: 2,
      category: "Scope",
      question: "Would you rather wear all engineering hats or specialize deeply in one layer?",
      options: [
        { id: "q2_a", text: "I want to be a full-stack maker: frontend, backend, database, and launch", domain_scores: { fullstack: 5 } },
        { id: "q2_b", text: "Deep dive into backend databases, system design, and API concurrency", domain_scores: { backend: 4 } },
        { id: "q2_c", text: "Master UI engineering, interaction design, and client-side performance", domain_scores: { frontend: 4 } },
        { id: "q2_d", text: "Specialize in modern generative AI, transformers, and LLM applications", domain_scores: { ai_ml: 5 } }
      ]
    }
  ];
}
