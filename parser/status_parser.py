import json
from collections import defaultdict
from datetime import datetime
import re

def parse_status_log(log_path):
    result = defaultdict(lambda: defaultdict(int))
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                log = json.loads(line)
                timestamp = datetime.fromisoformat(log["timestamp"])
                status_code = int(log["status_code"])
                hour_key = timestamp.replace(minute=0, second=0, microsecond=0)
                result[hour_key][status_code] += 1
            except (json.JSONDecodeError, KeyError, ValueError):
                continue
    return result

def parse_text_status(log_path):
    result = defaultdict(lambda: defaultdict(int))
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"\[(.*?)\] ✅ (https?://[^\s]+) OK - Status (\d+)", line)
            if match:
                timestamp_str, url, status_code = match.groups()
                try:
                    timestamp = datetime.fromisoformat(timestamp_str)
                    hour_key = timestamp.replace(minute=0, second=0, microsecond=0)
                    result[hour_key][int(status_code)] += 1
                except ValueError:
                    continue
    return result
