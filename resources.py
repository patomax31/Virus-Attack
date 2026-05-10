import os
import sys
from pathlib import Path


APP_DIR_NAME = "Virus-Attack"


def get_base_path():
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parent


def resource_path(*parts):
    return str(get_base_path().joinpath(*parts))


def configure_runtime_paths():
    # Keep legacy relative asset paths working in source and bundled modes.
    os.chdir(get_base_path())


def get_user_data_dir():
    home = Path.home()
    if sys.platform == "darwin":
        return home / "Library" / "Application Support" / APP_DIR_NAME
    if sys.platform.startswith("win"):
        appdata = os.environ.get("APPDATA")
        if appdata:
            return Path(appdata) / APP_DIR_NAME
        return home / "AppData" / "Roaming" / APP_DIR_NAME
    xdg_data_home = os.environ.get("XDG_DATA_HOME")
    if xdg_data_home:
        return Path(xdg_data_home) / APP_DIR_NAME
    return home / ".local" / "share" / APP_DIR_NAME


def user_data_file(filename):
    data_dir = get_user_data_dir()
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / filename
