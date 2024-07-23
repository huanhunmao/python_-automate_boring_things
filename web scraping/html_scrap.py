import requests
import bs4

# 添加请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

res = requests.get('https://nostarch.com', headers=headers)
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup)) # <class 'bs4.BeautifulSoup'>
