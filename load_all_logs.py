import os
import sys
import glob
from main import insert_status, insert_errors
from parser.status_parser import parse_status_log, parse_text_status
from parser.error_parser import parse_text_errors
from utils.helpers import extract_hostname_from_path

def process_file(log_path):
    hostname = extract_hostname_from_path(log_path)

    if log_path.endswith(".json.log"):
        result = parse_status_log(log_path)
        if result:
            print(f"✅ Inserisco status JSON: {log_path}")
            insert_status(hostname, result)
        else:
            print(f"⚠️  Nessun dato status JSON in: {log_path}")
    elif log_path.endswith(".log"):
        status_result = parse_text_status(log_path)
        error_result = parse_text_errors(log_path, hostname)

        if status_result:
            print(f"✅ Inserisco status testo: {log_path}")
            insert_status(hostname, status_result)
        else:
            print(f"⚠️  Nessun dato status testo in: {log_path}")

        if error_result:
            print(f"✅ Inserisco errori: {log_path}")
            insert_errors(error_result)
        else:
            print(f"⚠️  Nessun dato errori in: {log_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python load_all_logs.py <log_dir_or_glob>")
        sys.exit(1)

    for pattern in sys.argv[1:]:
        for file in sorted(glob.glob(pattern)):
            if os.path.isfile(file):
                print(f"📄 Analizzo {file}...")
                process_file(file)
