# run.py
import argparse
from src.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description="Agentic FB Performance Analyst")
    parser.add_argument("query", type=str, help="User instruction, e.g. 'Analyze ROAS drop in Feb'")
    args = parser.parse_args()

    orchestrator = Orchestrator()
    result = orchestrator.run(args.query)

    print("\n=== RUN COMPLETED ===")
    print("Insights saved to: reports/insights.json")
    print("Creative ideas saved to: reports/creatives.json")
    print("Human-readable report saved to: reports/report.md")

if __name__ == "__main__":
    main()
