# src/utils.py
import yaml
import os
import json
from datetime import datetime

def load_config(path: str = "config/config.yaml") -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def save_json(obj, path: str):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)

def append_log(record: dict, logs_dir: str = "logs"):
    ensure_dir(logs_dir)
    path = os.path.join(logs_dir, "run_log.jsonl")
    record = {**record, "ts": datetime.utcnow().isoformat()}
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
