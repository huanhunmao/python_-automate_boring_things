from selenium import webdriver

# 指定GeckoDriver的路径，如果已经在系统环境变量中设置，可以省略
# gecko_path = '/path/to/geckodriver'

browser = webdriver.Chrome()  # executable_path=gecko_path
browser.get('https://inventwithpython.com')
try:
    # 查找页面上的元素
    elem = browser.find_element_by_class_name(' cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

# 检查页面标题，确保页面成功加载
print(browser.title) # Invent with Python

# 关闭浏览器
browser.quit()
