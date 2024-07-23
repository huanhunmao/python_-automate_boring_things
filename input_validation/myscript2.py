import pyinputplus as pyip

# 限制输入偶数
# response = pyip.inputNum(blockRegexes=[r'[02468]$'])

# 限制输入单词
response1 = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
blockRegexes=[r'cat'])