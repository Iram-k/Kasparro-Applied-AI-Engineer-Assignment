# src/orchestrator.py
from src.utils import load_config, save_json, ensure_dir, append_log
from src.agents.data_agent import DataAgent
from src.agents.planner import PlannerAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator import EvaluatorAgent
from src.agents.creative_agent import CreativeAgent
import os
import pandas as pd

class Orchestrator:
    def __init__(self):
        self.config = load_config()
        self.data_agent = DataAgent(self.config)
        self.planner = PlannerAgent()
        self.insight_agent = InsightAgent()
        self.evaluator = EvaluatorAgent(self.config)
        self.creative_agent = CreativeAgent()

        ensure_dir(self.config["output"]["reports_dir"])
        ensure_dir(self.config["output"]["logs_dir"])

    def run(self, user_query: str):
        # 1) Data loading & basic summary
        df = self.data_agent.load_data()
        data_summary = self.data_agent.basic_summary()

        # 2) Planning
        plan = self.planner.run(user_query, data_summary)

        # 3) Execute plan steps (simple, sequential)
        roas_trend = self.data_agent.roas_trend(freq="D")
        campaign_summary = self.data_agent.campaign_summary()

        # Convert small summaries to text for prompt-style consumption
        roas_trend_desc = roas_trend.head(10).to_markdown(index=False)
        campaign_summary_desc = campaign_summary.head(15).to_markdown(index=False)

        # 4) Insights (hypotheses)
        insights = self.insight_agent.run(
            roas_trend_summary=roas_trend_desc,
            segment_summary=campaign_summary_desc
        )

        # 5) Validation
        data_context = {}  # could hold real baseline vs current deltas
        validated_insights = self.evaluator.run(insights, data_context)

        # 6) Creative recommendations
        thr = self.config["metrics"]["ctr_drop_pct_threshold"]
        # Use a rough CTR threshold based on global average
        global_ctr = df["ctr"].mean()
        ctr_threshold = global_ctr * (1 - thr)
        low_ctr_df = self.data_agent.low_ctr_segments(ctr_threshold).head(5)

        # For now we skip real "winning messages" mining; just pass empty list
        creative_recs = self.creative_agent.run(low_ctr_df, winning_messages_example=[])

        # 7) Build human-readable report
        report_md = self._build_report_markdown(user_query, data_summary,
                                                validated_insights, creative_recs)

        # 8) Save outputs
        reports_dir = self.config["output"]["reports_dir"]
        save_json(validated_insights, os.path.join(reports_dir, "insights.json"))
        save_json(creative_recs, os.path.join(reports_dir, "creatives.json"))
        with open(os.path.join(reports_dir, "report.md"), "w", encoding="utf-8") as f:
            f.write(report_md)

        append_log({"event": "run_completed", "user_query": user_query})

        return {
            "insights": validated_insights,
            "creatives": creative_recs,
            "report_markdown": report_md
        }

    def _build_report_markdown(self, query, data_summary, insights, creatives):
        lines = []
        lines.append(f"# Facebook Performance Analysis\n")
        lines.append(f"**User query:** {query}\n")
        lines.append("## 1. Dataset Overview")
        lines.append(f"- Rows analyzed: **{data_summary['rows']}**")
        lines.append(f"- Date range: **{data_summary['date_min']} → {data_summary['date_max']}**")
        lines.append(f"- Avg ROAS: **{data_summary['mean_roas']:.2f}**")
        lines.append(f"- Avg CTR: **{data_summary['mean_ctr']:.4f}**\n")

        lines.append("## 2. Key Performance Insights")
        for ins in insights:
            lines.append(f"### {ins['title']}")
            lines.append(f"- Hypothesis: {ins['hypothesis']}")
            lines.append(f"- Confidence: **{ins['confidence']:.2f}**")
            lines.append(f"- Validated: **{ins['validated']}**")
            if "evidence" in ins:
                lines.append(f"- Evidence: {ins['evidence'].get('description','')}")
            lines.append("")

        lines.append("## 3. Creative Recommendations")
        for c in creatives:
            lines.append(f"### Campaign: {c['campaign_name']}")
            lines.append(f"- Reason for recommendation: {c['reason']}")
            for idx, s in enumerate(c["suggestions"], start=1):
                lines.append(f"  - **Idea {idx}**")
                lines.append(f"    - Headline: {s['headline']}")
                lines.append(f"    - Primary Text: {s['primary_text']}")
                lines.append(f"    - CTA: {s['cta']}")
            lines.append("")

        lines.append("## 4. Next Steps for the Marketer")
        lines.append("- A/B test new creatives against current best performers.")
        lines.append("- Reallocate spend away from persistently low-ROAS campaigns.")
        lines.append("- Monitor ROAS and CTR for 7–14 days post-change.\n")

        return "\n".join(lines)
