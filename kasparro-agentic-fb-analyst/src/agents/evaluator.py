# src/agents/evaluator.py
from .base import Agent
import numpy as np

class EvaluatorAgent(Agent):
    def __init__(self, config: dict):
        super().__init__("EvaluatorAgent")
        self.config = config

    def run(self, insights: list, data_context: dict) -> list:
        """
        data_context can contain precomputed numbers like baseline vs current deltas.
        Here we just attach a 'validated' flag based on confidence threshold.
        """
        validated = []
        for ins in insights:
            conf = ins.get("confidence", 0.5)
            validated.append({
                **ins,
                "validated": conf >= 0.6,
                "validation_details": {
                    "rule": "confidence >= 0.6",
                    "passed": conf >= 0.6
                }
            })
        return validated
