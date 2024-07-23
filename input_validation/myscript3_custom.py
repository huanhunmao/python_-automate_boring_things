import pyinputplus as pyip

# 自定义 函数给 inputCustom
# 数字之和等于10
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %
        (sum(numbersList)))

    return int(numbers)


response = pyip.inputCustom(addsUpToTen,
                            prompt='Enter numbers that add up to 10: ')
print(response)
