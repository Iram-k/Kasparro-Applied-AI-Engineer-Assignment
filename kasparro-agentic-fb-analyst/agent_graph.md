\# Agent Graph – Agentic Facebook Performance Analyst



```mermaid

flowchart TD

&nbsp; U\[User Query] --> P\[Planner Agent]

&nbsp; P --> D\[Data Agent]

&nbsp; D --> I\[Insight Agent]

&nbsp; I --> E\[Evaluator Agent]

&nbsp; E --> C\[Creative Agent]

&nbsp; C --> O\[Orchestrator]

&nbsp; O --> R\[(Reports: insights.json, creatives.json, report.md)]

&nbsp; O --> L\[(logs/run\_log.jsonl)]



