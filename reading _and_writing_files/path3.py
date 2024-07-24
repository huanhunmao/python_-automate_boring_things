from pathlib import Path
import os

print(os.path.abspath('.'))

print(os.path.relpath('marxu', 'src/marx')) # ../../marxu