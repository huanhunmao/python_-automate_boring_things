import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res)) # <class 'requests.models.Response'>

print(res.status_code == requests.codes.ok) # True

print(len(res.text)) # 178978

print(res.text[:250]) # 拿到一些内容