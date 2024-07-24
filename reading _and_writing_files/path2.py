from pathlib import Path
import os

print(Path.cwd()) # /Users/fhj/Desktop/Github/python_automate_boring_things/reading _and_writing_files

# 用于改变当前工作目录
# os.chdir('/Users/fhj/Desktop/Github/python_automate_boring_things/')
# Path.cwd() # /Users/fhj/Desktop/Github/python_automate_boring_things/reading _and_writing_files

# home
print(Path.home()) # /Users/fhj

# 相对路径/绝对路径
print(Path.cwd().is_absolute()) # True
print(Path('spam/bacon/eggs').is_absolute()) # False

print(Path('my/relative/path')) # my/relative/path
print(Path.cwd() / Path('my/relative/path')) # /Users/fhj/Desktop/Github/python_automate_boring_things/reading _and_writing_files/my/relative/path

