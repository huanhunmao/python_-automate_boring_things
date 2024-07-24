from pathlib import Path

p = Path('text.txt')
p.write_text('Hello, world')

print(p.read_text()) # Hello, world