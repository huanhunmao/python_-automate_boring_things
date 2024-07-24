from pathlib import Path

print(str(Path('spam', 'bacon', 'eggs'))) # 层级 spam/bacon/eggs

myfiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myfiles:
    print(Path(r'marxu/', filename))
    # marxu / accounts.txt
    # marxu / details.csv
    # marxu / invite.docx


# 可以这样用 拼起来 路径
path = Path('spam') / 'bacon' / 'eggs'
print(path) # spam/bacon/eggs

# 还可以这样
homeFolder = Path('marxu/')
subFolder = Path('spam')
print(homeFolder / subFolder) # marxu/spam