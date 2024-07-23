import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.raise_for_status()) # None 没有错误
# 打开或创建一个名为RomeoAndJuliet.txt的文件，并以二进制写入模式（'wb'）打开
playFile = open('RomeoAndJuliet.txt', 'wb')
# 每次读取100,000字节（100 KB）的数据块
for chunk in res.iter_content(100000):
    playFile.write(chunk)

# 关闭文件，确保所有数据都被写入并释放系统资源
playFile.close()