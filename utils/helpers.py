import os

def extract_hostname_from_path(path):
    return os.path.basename(path).replace(".log", "")
