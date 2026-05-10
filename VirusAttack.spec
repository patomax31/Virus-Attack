# -*- mode: python ; coding: utf-8 -*-
import sys


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets', 'assets'),
        ('texts.json', '.'),
        ('progress.json', '.'),
        ('font.ttf', '.'),
    ],
    hiddenimports=['cv2', 'pygame'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

icon_file = 'assets/icons/VirusAttack.icns' if sys.platform == 'darwin' else 'assets/icons/VirusAttack.ico'

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='VirusAttack',
    icon=icon_file,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

if sys.platform == 'darwin':
    app = BUNDLE(
        exe,
        name='VirusAttack.app',
        icon=icon_file,
        bundle_identifier='com.virusattack.game',
    )
else:
    coll = COLLECT(
        exe,
        a.binaries,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='VirusAttack',
    )
