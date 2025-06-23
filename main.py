from config.db_config import DB_CONF
from parser.status_parser import parse_status_log, parse_text_status
from parser.error_parser import parse_text_errors
from utils.helpers import extract_hostname_from_path
import mysql.connector
import sys
import os

def insert_status(hostname, status_dict):
    conn = mysql.connector.connect(**DB_CONF)
    cursor = conn.cursor()
    total_inserted = 0
    for hour_str, counter in status_dict.items():
        for code, count in counter.items():
            try:
                cursor.execute("""
                    INSERT INTO http_status (hostname, log_date, status_code, count)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE count = VALUES(count)
                """, (hostname, hour_str, code, count))
                total_inserted += 1
            except mysql.connector.Error as e:
                print(f"❌ ERRORE insert_status: {e} — {hostname}, {hour_str}, {code}")
    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Status inseriti per {hostname}: {total_inserted} righe")

def insert_errors(error_rows):
    conn = mysql.connector.connect(**DB_CONF)
    cursor = conn.cursor()
    total_inserted = 0
    for row in error_rows:
        try:
            cursor.execute("""
                INSERT INTO page_errors (hostname, log_date, url, error_type, raw_error)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE raw_error = VALUES(raw_error)
            """, row)
            total_inserted += 1
        except mysql.connector.Error as e:
            print(f"❌ ERRORE insert_errors: {e} — {row}")
    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Errori inseriti: {total_inserted} righe")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python main.py <log_file>")
        sys.exit(1)

    log_path = sys.argv[1]
    if not os.path.isfile(log_path):
        print(f"❌ File non trovato: {log_path}")
        sys.exit(1)

    hostname = extract_hostname_from_path(log_path)

    if log_path.endswith(".json.log"):
        result = parse_status_log(log_path)
        if result:
            insert_status(hostname, result)
        else:
            print(f"⚠️ Nessun dato status trovato in {log_path}")
    else:
        status_data = parse_text_status(log_path)
        if status_data:
            insert_status(hostname, status_data)
        else:
            print(f"⚠️ Nessun dato status testuale in {log_path}")

        error_data = parse_text_errors(log_path, hostname)
        if error_data:
            insert_errors(error_data)
        else:
            print(f"⚠️ Nessun dato errori trovato in {log_path}")