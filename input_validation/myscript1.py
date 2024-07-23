import pyinputplus as pyip

# 提示用户输入一个数字，并且最多允许两次尝试
# try:
#     response = pyip.inputNum('Enter a number: ', limit=2)
#     print('You entered:', response)
# except pyip.RetryLimitException:
#     print('You have exceeded the maximum number of attempts')
#

# 如果用户在 10 秒内没有输入一个有效的数字，程序将会引发 pyinputplus.TimeoutException 异常
# try:
#     response = pyip.inputNum('Enter a number: ', timeout=10)
#     print('You entered:', response)
# except pyip.TimeoutException:
#     print('You have exceeded the time limit')


# response = pyip.inputNum(limit=2, default='N/A')

# 运行正则
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
response1 = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])