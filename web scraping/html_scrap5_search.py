import requests
import sys
import webbrowser
import bs4

# 检查是否有传入参数
if len(sys.argv) < 2:
    print("Usage: python script_name.py search_term")
    sys.exit()

search_term = ' '.join(sys.argv[1:])
print('Searching for:', search_term)

# 构造搜索 URL  搜索 pip 包
url = f'https://pypi.org/search/?q={search_term}'

# 发起请求
res = requests.get(url)
res.raise_for_status()

# 解析 HTML
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# 提取搜索结果链接
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
print('Number of links to open:', numOpen)

# 打开前五个搜索结果的链接
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening:', urlToOpen)
    webbrowser.open(urlToOpen)


# 示例例子和结果
# python html_scrap5_search.py requests
# python html_scrap5_search.py world
# Searching for: world
# Number of links to open: 5
# Opening: https://pypi.org/project/world/
# Opening: https://pypi.org/project/pixel2world/
# Opening: https://pypi.org/project/pic2world/
# Opening: https://pypi.org/project/pixel-world/
# Opening: https://pypi.org/project/print-0-world/
