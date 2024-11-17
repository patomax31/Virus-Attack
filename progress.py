import json

PROGRESS_FILE = 'progress.json'

def load_progress():
    try:
        with open(PROGRESS_FILE, "r") as file:
            progress = json.load(file)
            if "level" not in progress:
                progress["level"] = 1
            return progress
    except FileNotFoundError:
        return {"level": 1}

def save_progress(progress):
    with open(PROGRESS_FILE, "w") as file:
        json.dump(progress, file)

def get_current_level():
    progress = load_progress()
    return progress["level"]

def set_current_level(level):
    progress = load_progress()
    progress["level"] = level
    save_progress(progress)