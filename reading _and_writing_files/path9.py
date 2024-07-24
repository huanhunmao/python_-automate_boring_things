from pathlib import Path

winDir = Path('marxu/test')
print(winDir.exists()) # False
print(winDir.is_dir()) # False
print(winDir.is_file()) # False


winDir2 = Path('text.txt')
print(winDir2.exists()) # True
print(winDir2.is_dir()) # False
print(winDir2.is_file()) # True