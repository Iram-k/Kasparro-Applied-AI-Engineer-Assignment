# src/agents/insight_agent.py
from .base import Agent
from pathlib import Path
import json

class InsightAgent(Agent):
    def __init__(self, prompt_dir: str = "prompts"):
        super().__init__("InsightAgent")
        self.prompt_path = Path(prompt_dir) / "insight.md"

    def run(self, roas_trend_summary: str, segment_summary: str) -> list:
        """
        In a real system, we would call an LLM with the contents of insight.md,
        pass roas_trend_summary and segment_summary as context,
        and ask for JSON output.

        For this assignment, we construct 1–2 example insights programmatically.
        """
        insights = [
            {
                "id": "insight_1",
                "title": "ROAS drop linked to CTR decline in key campaigns",
                "hypothesis": (
                    "Between early and mid period, ROAS decreased primarily because "
                    "CTR fell for several high-spend campaigns while CPC increased."
                ),
                "evidence": {
                    "description": "Segment summary shows lower CTR and ROAS for top spenders in later dates.",
                    "metrics_used": ["roas", "ctr", "cpc"]
                },
                "confidence": 0.8
            }
        ]
        return insights
