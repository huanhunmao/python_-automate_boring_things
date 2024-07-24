from pathlib import Path

print(Path.cwd()) # /Users/fhj/Desktop/Github/python_automate_boring_things/reading _and_writing_files
print(Path.cwd().parents[0]) # /Users/fhj/Desktop/Github/python_automate_boring_things
print(Path.cwd().parents[1]) # /Users/fhj/Desktop/Github
print(Path.cwd().parents[2]) # /Users/fhj/Desktop
print(Path.cwd().parents[3]) # /Users/fhj
print(Path.cwd().parents[4]) # /Users
print(Path.cwd().parents[5]) # /Users
print(Path.cwd().parents[6]) # IndexError: 6