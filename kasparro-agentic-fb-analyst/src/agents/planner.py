# src/agents/planner.py
from .base import Agent
from pathlib import Path

class PlannerAgent(Agent):
    def __init__(self, prompt_dir: str = "prompts"):
        super().__init__("PlannerAgent")
        self.prompt_path = Path(prompt_dir) / "planner.md"

    def run(self, user_query: str, data_summary: dict) -> dict:
        """
        In a real system, this would call an LLM with planner.md.
        For this assignment, we return a fixed but structured plan.
        """
        # You can extend logic later; for now we keep deterministic.
        plan = {
            "goal": user_query,
            "subtasks": [
                {
                    "id": "data_trend",
                    "type": "data_analysis",
                    "description": "Compute ROAS trend by date and detect major drops."
                },
                {
                    "id": "segment_breakdown",
                    "type": "segmentation",
                    "description": "Break down ROAS, CTR, CPC, CVR by campaign and audience_type."
                },
                {
                    "id": "generate_insights",
                    "type": "hypothesis",
                    "description": "Generate hypotheses explaining ROAS changes using segment summaries."
                },
                {
                    "id": "validate_insights",
                    "type": "validation",
                    "description": "Quantitatively validate each hypothesis and assign confidence."
                },
                {
                    "id": "creative_ideas",
                    "type": "creative",
                    "description": "Propose new creative directions for low-CTR, high-spend campaigns."
                }
            ]
        }
        return plan
