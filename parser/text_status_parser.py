import re
from collections import defaultdict
from datetime import datetime

def parse_text_status(log_path):
    result = defaultdict(lambda: defaultdict(int))

    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"\[(.*?)\] ❌ (https?://[^\s]+)", line)
            if match:
                timestamp_str, url = match.groups()
                try:
                    timestamp = datetime.fromisoformat(timestamp_str)
                    hour_key = timestamp.replace(minute=0, second=0, microsecond=0)
                    result[hour_key][408] += 1  # 408 = Request Timeout
                except ValueError:
                    continue

    return result
