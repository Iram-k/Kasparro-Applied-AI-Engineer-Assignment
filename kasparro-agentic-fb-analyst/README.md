Kasparro – Agentic Facebook Performance Analyst

Applied AI Engineer Assignment (Multi-Agent System for ROAS Diagnostics)



This project implements a multi-agent analytical system that autonomously analyzes Facebook Ads performance, diagnoses reasons behind ROAS changes, and generates data-driven creative recommendations.

It is designed according to the requirements defined in the Kasparro Applied AI Engineer Assignment – Agentic Facebook Performance Analyst brief.



The system simulates an agentic reasoning pipeline using structured Python modules, deterministic planning logic, and modular agents for data analysis, insight generation, validation, and creative ideation.



🚀 1. Project Overview



This system answers questions such as:



“Why did ROAS drop this week?”



“Which campaigns caused the decline?”



“What creative improvements can we test?”



It uses the provided Facebook Ads dataset (undergarments vertical) to:



Diagnose why ROAS changed over time.



Identify quantitative drivers, such as:



CTR drop



CPC increase



Creative fatigue



Audience-level shifts



Spend concentration in underperforming campaigns



Generate creative ideas for low-CTR campaigns, grounded in patterns found in existing messaging.



The output is saved as:



reports/insights.json



reports/creatives.json



reports/report.md



🧠 2. Multi-Agent Architecture



The system consists of five modular agents, orchestrated by a central controller:



1\. Planner Agent



Breaks user query into structured subtasks

(e.g., trend detection → segmentation → insights → validation → creative generation).



2\. Data Agent



Handles:



CSV loading



ROAS trend calculation



Campaign-level summaries



Low-CTR segment identification



3\. Insight Agent



Generates high-level hypotheses explaining ROAS changes using data summaries.



4\. Evaluator Agent



Validates hypotheses using:



Metric deltas



Threshold comparisons (from config)



Confidence logic



5\. Creative Agent



Produces new creative recommendations (headline + primary text + CTA) for low-CTR, high-spend campaigns.



📁 3. Repository Structure

kasparro-agentic-fb-analyst/

│

├─ run.py

├─ requirements.txt

├─ README.md

├─ agent\_graph.md

│

├─ config/

│  └─ config.yaml

│

├─ data/

│  ├─ synthetic\_fb\_ads\_undergarments.csv

│  └─ README.md

│

├─ src/

│  ├─ orchestrator.py

│  ├─ utils.py

│  └─ agents/

│     ├─ base.py

│     ├─ planner.py

│     ├─ data\_agent.py

│     ├─ insight\_agent.py

│     ├─ evaluator.py

│     └─ creative\_agent.py

│

├─ reports/

│  ├─ insights.json

│  ├─ creatives.json

│  └─ report.md

│

├─ logs/

│  └─ run\_log.jsonl

│

└─ prompts/

&nbsp;  ├─ planner.md

&nbsp;  ├─ insight.md

&nbsp;  ├─ evaluator.md

&nbsp;  └─ creative.md



⚙️ 4. Installation \& Setup

1\. Clone the repository

git clone <your-public-github-repo-url>

cd kasparro-agentic-fb-analyst



2\. Install dependencies

pip install -r requirements.txt



3\. Verify data file



Ensure the dataset is present in:



data/synthetic\_fb\_ads\_undergarments.csv



▶️ 5. How to Run



Run the agentic system using a natural language query:



python run.py "Analyze ROAS drop and propose creative improvements"





The system will generate:



➤ reports/insights.json



Structured hypotheses with evidence \& validation flags.



➤ reports/creatives.json



Creative recommendations for low-performing campaigns.



➤ reports/report.md



Clean marketer-friendly report summarizing findings.



➤ logs/run\_log.jsonl



Evidence \& observability logs.



📊 6. Example Output (Summarized)

Insights (insights.json)

\[

&nbsp; {

&nbsp;   "id": "insight\_1",

&nbsp;   "title": "ROAS drop linked to CTR decline in key campaigns",

&nbsp;   "hypothesis": "ROAS decreased because CTR fell for high-spend campaigns while CPC increased.",

&nbsp;   "confidence": 0.8,

&nbsp;   "validated": true

&nbsp; }

]



Creative Recommendations (creatives.json)

\[

&nbsp; {

&nbsp;   "campaign\_name": "MEN BOLD COLORS DROP",

&nbsp;   "reason": "Low CTR and below-average ROAS.",

&nbsp;   "suggestions": \[

&nbsp;     {

&nbsp;       "headline": "Color that pops. Comfort that stays.",

&nbsp;       "primary\_text": "Seamless trunks designed for all-day movement.",

&nbsp;       "cta": "Shop the Bold Collection"

&nbsp;     }

&nbsp;   ]

&nbsp; }

]



🔍 7. Configuration \& Reproducibility



All thresholds and settings are stored in:



config/config.yaml





Key reproducibility elements:



seeded sampling (random\_seed)



deterministic fallback agent outputs



pinned versions in requirements.txt



separate prompts directory



logging via JSONL



🧪 8. Testing



A lightweight test is included in:



tests/test\_evaluator.py





Run tests with:



pytest



🧩 9. Git Hygiene



Minimum submission requirements followed:



✔ Multiple meaningful commits



✔ Release tag: v1.0



✔ Pull Request titled “self-review”



✔ Clear commit history



✔ No large files committed



📝 10. Notes \& Limitations



LLM calls are simulated for assignment purposes.



Only summary data is passed to generative agents—never the full dataset.



Creative outputs are inspired by patterns in provided creative messaging.



The system can be extended with:



Real LLM calls (OpenAI, Anthropic)



Langfuse tracing



Memory between runs



🙌 11. Author



Iram Khan

Applied AI Engineer — Assignment Submission

Kasparro Agentic Marketing Analyst System



