# 🎮  About pygame
Welcome to the official repository of an educational game developed in Python with Pygame. This project is designed to raise awareness about the importance of health and wellness, focusing on promoting healthy habits and well-being for all.

# 🎯 About the game
In this game, you will embark on a mission to protect a hospital from dangerous viruses and bacteria that threaten the health of patients. Throughout the game, you'll face various challenges in a fast-paced environment, defending against waves of germs while ensuring the well-being of everyone inside.

# 📜 License
This proyect is under the MIT License.

# 📦 Build executables (Windows, macOS, Linux)
This repository now includes a PyInstaller setup to build portable executables for all major desktop systems.

## Local build
1. Install Python 3.11.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

Optional (regenerate Windows/Linux icon from source image):

```bash
python3 tools/generate_app_icons.py
```

3. Build executable:

```bash
python3 -m PyInstaller VirusAttack.spec --clean
```

4. Output folder:
- `dist/VirusAttack/`

Run the app from that folder:
- Windows: `dist/VirusAttack/VirusAttack.exe`
- macOS/Linux: `dist/VirusAttack/VirusAttack`

## GitHub Actions build
The workflow file is at `.github/workflows/build.yml` and generates artifacts for:
- Windows
- macOS
- Linux

How to use:
1. Push changes to `main`/`master` or open a PR.
2. Or run manually from the Actions tab using `Build Executables`.
3. Download the generated artifact zip from the workflow run.

## Notes
- Executables are portable (no installer in this phase).
- Code signing and notarization are not included yet.
- Saved progress is written to an OS user-data folder instead of the bundled app folder.
