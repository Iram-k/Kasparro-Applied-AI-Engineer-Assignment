# src/agents/creative_agent.py
from .base import Agent
from pathlib import Path

class CreativeAgent(Agent):
    def __init__(self, prompt_dir: str = "prompts"):
        super().__init__("CreativeAgent")
        self.prompt_path = Path(prompt_dir) / "creative.md"

    def run(self, low_ctr_campaigns_df, winning_messages_example: list) -> list:
        """
        Normally: call LLM with examples to generate new creatives.
        Here: produce structured example ideas.
        """
        creatives = []
        for _, row in low_ctr_campaigns_df.iterrows():
            creatives.append({
                "campaign_name": row["campaign_name"],
                "reason": f"Low CTR ({row['avg_ctr']:.4f}) and below-average ROAS ({row['avg_roas']:.2f}).",
                "suggestions": [
                    {
                        "headline": "Comfort that actually lasts all day",
                        "primary_text": "Soft fabric, zero ride-up, and bold colors that feel as good as they look.",
                        "cta": "Shop Now"
                    },
                    {
                        "headline": "Stop adjusting. Start moving.",
                        "primary_text": "Seamless design that stays in place, whether you're at the gym or at work.",
                        "cta": "Try It Today"
                    }
                ]
            })
        return creatives
