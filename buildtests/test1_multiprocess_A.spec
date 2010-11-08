# -*- mode: python -*-

print 'TESTING MULTIPROCESS FEATURE: file A (onefile pack) depends on file B (onefile pack).'

__testname__ = 'test1_multiprocess_A'
__testdep__ = 'test1_multiprocess_B'

a = Analysis([os.path.join(HOMEPATH,'support', '_mountzlib.py'), os.path.join(HOMEPATH,'support', 'useUnicode.py'), __testname__ + '.py'],
             pathex=['.'])
b = Analysis([os.path.join(HOMEPATH,'support', '_mountzlib.py'), os.path.join(HOMEPATH,'support', 'useUnicode.py'), __testdep__ + '.py'],
             pathex=['.'])

MERGE(b, a)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          a.dependencies,
          name=os.path.join('dist', __testname__),
          debug=False,
          strip=False,
          upx=True,
          console=1 )
                    
pyzB = PYZ(b.pure)
exeB = EXE(pyzB,
          b.scripts,
          b.binaries,
          b.zipfiles,
          b.datas,
          b.dependencies,
          name=os.path.join('dist', __testdep__),
          debug=False,
          strip=False,
          upx=True,
          console=1 )

