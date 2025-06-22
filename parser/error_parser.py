import re
from datetime import datetime

def classify_error(error_text):
    if "ERR_PROXY_CONNECTION_FAILED" in error_text:
        return "proxy_failed"
    elif "ERR_TIMED_OUT" in error_text or "Timeout" in error_text:
        return "timeout"
    elif "ControlPort" in error_text:
        return "controlport"
    else:
        return "altro"

def parse_text_errors(log_path, hostname):
    result = []

    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"\[(.*?)\] ❌ (https?://[^\s]+).*?Errore: (.+)", line)
            if match:
                timestamp_str, url, error_text = match.groups()
                try:
                    timestamp = datetime.fromisoformat(timestamp_str)
                    error_type = classify_error(error_text.strip())
                    result.append((hostname, timestamp, url, error_type, error_text.strip()))
                except ValueError:
                    continue
    return result
