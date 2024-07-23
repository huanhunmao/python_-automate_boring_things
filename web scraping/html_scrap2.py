import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# print(type(exampleSoup)) # <class 'bs4.BeautifulSoup'>

# 使用 select 拿到 element
elems = exampleSoup.select('#author')
print(type(elems)) # <class 'bs4.element.ResultSet'>

print(len(elems))  # 1

print(type(elems[0])) # <class 'bs4.element.Tag'>

print(elems[0].getText()) # Al Sweigart

print(elems[0].attrs) # {'id': 'author'}