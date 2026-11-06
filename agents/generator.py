# ==============================================================================
# Module: Cover Letter & Communication Synthesis Agent
# Author: Harpreet Singh
# Description: Generates targeted, personalized corporate cover letters from candidate profiles.
# ==============================================================================

class CoverLetterGeneratorAgent:
    def __init__(self, tone: str = "Professional & Impact-Driven"):
        self.tone = tone

    def generate(self, candidate_name: str, target_role: str, company_name: str, core_achievements: list) -> str:
        achievements_formatted = "
".join([f"  • {ach}" for ach in core_achievements])
        return (
            f"Dear Hiring Team at {company_name},

"
            f"I am writing to express my enthusiastic interest in the {target_role} position. "
            f"With a strong track record of engineering scalable, secure systems and designing advanced AI-driven workflows, "
            f"I am confident in my ability to deliver immediate value to your team.

"
            f"Key Highlights of My Background:
{achievements_formatted}

"
            f"Your mission at {company_name} aligns closely with my dedication to continuous technical excellence and robust engineering. "
            f"I welcome the opportunity to discuss how my technical leadership can support your upcoming product roadmap.

"
            f"Sincerely,
{candidate_name}
"
        )

if __name__ == "__main__":
    gen = CoverLetterGeneratorAgent()
    letter = gen.generate(
        candidate_name="Harpreet Singh",
        target_role="Lead AI Infrastructure Architect",
        company_name="CloudMatrix Labs",
        core_achievements=[
            "Architected low-latency correlation engines processing over 50,000 events/sec.",
            "Deployed production-grade multi-agent LLM systems with evaluation guardrails.",
            "Led cross-functional software initiatives combining engineering and computational data analysis."
        ]
    )
    print(letter)
