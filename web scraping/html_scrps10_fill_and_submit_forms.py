from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('http://localhost:63342/python_automate_boring_things/web%20scraping/html_scrap10_test.html?_ijt=et7fqs6p8sjv2omd43tjujs7ml&_ij_reload=RELOAD_ON_SAVE')

try:
    # 等待用户名输入框加载
    userElem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )
    userElem.send_keys('marxu')

    # 等待密码输入框加载
    passwordElem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    passwordElem.send_keys('password')

    # 提交表单
    passwordElem.submit()

    # 等待页面加载完成，检查页面是否跳转
    WebDriverWait(browser, 10).until(
        EC.url_changes('http://localhost:63342/python_automate_boring_things/web%20scraping/html_scrap10_test.html?_ijt=et7fqs6p8sjv2omd43tjujs7ml&_ij_reload=RELOAD_ON_SAVE')
    )

    # 检查页面上是否存在某个预期元素，例如一个特定的消息或标题
    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'success-message'))
    )
    assert success_message.text == '登录成功', "成功消息未出现或不匹配"
finally:
    browser.quit()
