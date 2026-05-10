from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ICON = ROOT / "assets" / "sprites" / "enemigo_enfrente_azul3.png"
ICONS_DIR = ROOT / "assets" / "icons"
ICO_OUTPUT = ICONS_DIR / "VirusAttack.ico"


def generate_ico() -> None:
    ICONS_DIR.mkdir(parents=True, exist_ok=True)
    image = Image.open(SOURCE_ICON).convert("RGBA")
    sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    image.save(ICO_OUTPUT, format="ICO", sizes=sizes)


if __name__ == "__main__":
    generate_ico()
