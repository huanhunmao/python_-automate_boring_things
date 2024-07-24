import os

calcFilePath = 'marxu/data/test/test.txt'
print(os.path.basename(calcFilePath)) # test.txt
print(os.path.dirname(calcFilePath)) # marxu/data/test
print(os.path.split(calcFilePath)) # ('marxu/data/test', 'test.txt')
# 或者这样拼起来
print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath))) # ('marxu/data/test', 'test.txt')

print(calcFilePath.split(os.sep)) # ['marxu', 'data', 'test', 'test.txt'] 这个不错
print('/usr/local/bin/'.split(os.sep)) # ['', 'usr', 'local', 'bin', '']