import re
from datetime import datetime

def parse_text_errors(file_path, hostname):
    pattern = re.compile(r'\[(.*?)\] ❌ (.*?) - Errore: (.*)')
    rows = []
    with open(file_path, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                ts_raw, url, error_text = match.groups()
                try:
                    log_dt = datetime.fromisoformat(ts_raw)
                except Exception:
                    continue
                error_type = classify_error(error_text)
                rows.append((hostname, log_dt, url, error_type, error_text.strip()))
    return rows

def classify_error(error_text):
    if "ERR_PROXY_CONNECTION_FAILED" in error_text:
        return "proxy_failed"
    elif "ERR_TIMED_OUT" in error_text or "Timeout" in error_text:
        return "timeout"
    elif "ControlPort" in error_text:
        return "controlport"
    else:
        return "altro"
