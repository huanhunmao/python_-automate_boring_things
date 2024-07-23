import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# print(type(exampleSoup)) # <class 'bs4.BeautifulSoup'>

# 使用 select 拿到 element
spanElem = exampleSoup.select('span')[0]

print(str(spanElem)) # '<span id="author">Al Sweigart</span>'

print(spanElem.get('id')) # author

# 检查spanElem对象的some_nonexistent_addr属性是否不存在或为None
print(spanElem.get('some_nonexistent_addr') == None) # True

print(spanElem.attrs) # {'id': 'author'}
