from selenium import webdriver
from selenium.webdriver.common.by import By

# 启动浏览器
browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')

# 单击页面上的链接
linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
print(type(linkElem))  # 输出元素类型
linkElem.click()  # 跟随 "Read Online for Free" 链接
