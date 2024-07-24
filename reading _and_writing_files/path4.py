from pathlib import Path

p = Path('/Users/marxu/al/spam.txt')

print(p.anchor) # /
print(p.name) # spam.txt
print(p.stem) # spam
print(p.suffix) # .txt
print(p.drive)