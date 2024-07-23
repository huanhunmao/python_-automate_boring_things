import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
  address = ' '.join(sys.argv[1:])
else:
  address = pyperclip.paste()

# 获取一个地址（URL），然后使用浏览器打开谷歌地图并在地图上显示该地址
webbrowser.open('https://www.google.com/maps/place/' + address)
