import os
import sys
import subprocess

log_dir = sys.argv[1]

for file in sorted(os.listdir(log_dir)):
    if file.endswith(".log"):
        print(f"Inserisco {file}...")
        subprocess.run(["python", "main.py", os.path.join(log_dir, file)])
