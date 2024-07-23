from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://login.metafilter.com')
userElem = browser.find_element_by_id('user_name')
userElem.send_keys('marxu')

passwordElem = browser.find_element_by_id('user_pass')
userElem.send_keys('password')
passwordElem.submit()