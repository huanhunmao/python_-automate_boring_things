import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# print(type(exampleSoup)) # <class 'bs4.BeautifulSoup'>

# 使用 select 拿到 element
pElems = exampleSoup.select('p')
# print(pElems[0])
# <p>Download my <strong>Python</strong> book from <a href="https://
# inventwithpython.com">my website</a>.</p>

# print(pElems[0].getText())
# Download my Python book from my website.

print(pElems[1])
# <p class="slogan">Learn Python the easy way!</p>

print(pElems[1].getText())
# Learn Python the easy way!