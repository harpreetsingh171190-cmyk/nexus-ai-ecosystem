# ==============================================================================
# Module: AI Recruitment & Candidate Evaluation Agent
# Author: Harpreet Singh
# Description: Automated resume parsing, candidate scoring, and structured ranking.
# ==============================================================================

import json
from typing import List, Dict, Any

class ResumeScreeningAgent:
    def __init__(self, job_title: str, required_skills: List[str], min_experience_years: int):
        self.job_title = job_title
        self.required_skills = [s.lower() for s in required_skills]
        self.min_experience_years = min_experience_years

    def evaluate_candidate(self, candidate_name: str, resume_text: str, years_exp: int) -> Dict[str, Any]:
        text_lower = resume_text.lower()
        matched = [skill for skill in self.required_skills if skill in text_lower]
        match_ratio = len(matched) / max(len(self.required_skills), 1)
        
        exp_score = min(years_exp / max(self.min_experience_years, 1), 1.5) * 40
        skills_score = match_ratio * 60
        total_score = round(exp_score + skills_score, 2)
        
        status = "Recommended" if total_score >= 75 else "Review" if total_score >= 50 else "Not Selected"
        
        return {
            "name": candidate_name,
            "job_applied": self.job_title,
            "matched_skills": matched,
            "missing_skills": [s for s in self.required_skills if s not in matched],
            "total_score": total_score,
            "status": status
        }

if __name__ == "__main__":
    agent = ResumeScreeningAgent(
        job_title="Full Stack AI Engineer",
        required_skills=["Python", "FastAPI", "React", "Docker", "Machine Learning"],
        min_experience_years=3
    )
    res = agent.evaluate_candidate(
        "Harpreet Singh",
        "Senior Developer experienced in Python, React, Docker, Machine Learning, thermal analysis, and microservices.",
        5
    )
    print("Candidate Evaluation Result:
", json.dumps(res, indent=2))
