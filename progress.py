import json
from resources import resource_path, user_data_file

PROGRESS_FILE = user_data_file("progress.json")
DEFAULT_PROGRESS = {"current_level": 1, "level": 1}


def _initial_progress():
    try:
        with open(resource_path("progress.json"), "r", encoding="utf-8") as file:
            bundled_progress = json.load(file)
            if isinstance(bundled_progress, dict):
                return bundled_progress
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return DEFAULT_PROGRESS.copy()

def load_progress():
    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as file:
            progress = json.load(file)
            if "level" not in progress:
                progress["level"] = 1
            if "current_level" not in progress:
                progress["current_level"] = progress["level"]
            return progress
    except FileNotFoundError:
        progress = _initial_progress()
        save_progress(progress)
        return progress
    except json.JSONDecodeError:
        progress = DEFAULT_PROGRESS.copy()
        save_progress(progress)
        return progress

def save_progress(progress):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as file:
        json.dump(progress, file)

def get_current_level():
    progress = load_progress()
    return progress["level"]

def set_current_level(level):
    progress = load_progress()
    progress["level"] = level
    save_progress(progress)