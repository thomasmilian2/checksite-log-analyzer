import sys
from pathlib import Path
import subprocess

log_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("logs")

if not log_dir.exists():
    print(f"Directory {log_dir} non trovata.")
    sys.exit(1)

for log_file in sorted(log_dir.glob("*.log")):
    print(f"Inserisco {log_file}...")
    subprocess.run(["python", "main.py", str(log_file)])
