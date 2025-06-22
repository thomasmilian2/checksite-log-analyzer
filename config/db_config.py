import os
from dotenv import load_dotenv

load_dotenv()

DB_CONF = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "checksite"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "checksite_logs")
}
