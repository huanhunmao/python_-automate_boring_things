import  os
from pathlib import Path

# 查找文件大小和文件夹内容
print(os.path.getsize('os_path6.py')) # 515
print(Path.cwd()) # /Users/fhj/Desktop/Github/python_automate_boring_things/reading _and_writing_files
print(os.listdir('/Users/fhj/Desktop/Github/python_automate_boring_things/reading _and_writing_files'))
# ['path3.py', 'path2.py', '__pycache__', 'path5.py', 'path4.py', 'os_path7.py', 'path.py', 'os_path6.py']

# 计算总的 size
totalSize = 0
path = '/Users/fhj/Desktop/Github/python_automate_boring_things/reading _and_writing_files'
for filename in os.listdir(path):
    totalSize = totalSize + os.path.getsize(os.path.join(path, filename))

print(totalSize) # 3286