import json
from collections import Counter
from datetime import datetime

def parse_status_log(file_path):
    status_hourly = {}
    with open(file_path, 'r') as f:
        for line in f:
            try:
                log = json.loads(line)
                status = int(log.get("status", 0))
                timestamp = datetime.fromisoformat(log["timestamp"])
                hour_key = timestamp.strftime("%Y-%m-%d %H:00:00")
                status_hourly.setdefault(hour_key, Counter())[status] += 1
            except Exception:
                continue
    return status_hourly
