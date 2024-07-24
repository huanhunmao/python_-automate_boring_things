import os
from pathlib import Path

p = Path('/Users/fhj/Desktop/Github/python_automate_boring_things/reading _and_writing_files')
print(p.glob('*.')) # <generator object Path.glob at 0x10247dc40>

# print(list(p.glob('*')))

print(list(p.glob('*.txt'))) # [PosixPath('/Users/fhj/Desktop/Github/python_automate_boring_things/reading _and_writing_files/text.txt')]
print(list(p.glob('*.docx'))) # [PosixPath('/Users/fhj/Desktop/Github/python_automate_boring_things/reading _and_writing_files/text.docx')


for textFilePathObj in p.glob('*.txt'):
    print(textFilePathObj)
    # / Users / fhj / Desktop / Github / python_automate_boring_things / reading
    # _and_writing_files / text2.txt
    # / Users / fhj / Desktop / Github / python_automate_boring_things / reading
    # _and_writing_files / text.txt

