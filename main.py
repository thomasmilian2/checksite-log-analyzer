from config.db_config import DB_CONF
from parser.status_parser import parse_status_log
from parser.error_parser import parse_text_errors
from utils.helpers import extract_hostname_from_path
import mysql.connector
import sys

def insert_status(hostname, status_dict):
    conn = mysql.connector.connect(**DB_CONF)
    cursor = conn.cursor()
    for hour_str, counter in status_dict.items():
        for code, count in counter.items():
            cursor.execute("""
                INSERT INTO http_status (hostname, log_date, status_code, count)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE count = count + VALUES(count)
            """, (hostname, hour_str, code, count))
    conn.commit()
    cursor.close()
    conn.close()

def insert_errors(error_rows):
    conn = mysql.connector.connect(**DB_CONF)
    cursor = conn.cursor()
    for row in error_rows:
        cursor.execute("""
            INSERT INTO page_errors (hostname, log_date, url, error_type, raw_error)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE raw_error = VALUES(raw_error)
        """, row)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    log_path = sys.argv[1]
    hostname = extract_hostname_from_path(log_path)

    if log_path.endswith(".json.log"):
        result = parse_status_log(log_path)
        insert_status(hostname, result)
    else:
        result = parse_text_errors(log_path, hostname)
        insert_errors(result)
