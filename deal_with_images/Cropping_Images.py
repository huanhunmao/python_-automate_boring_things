from PIL import Image

# 裁剪图片
catIm = Image.open('purpleImage.png')
croppedIm = catIm.crop((20, 20, 120, 120))
croppedIm.save('newImage.png')

# 复制图片
newCopy = croppedIm.copy()

print(newCopy.size) # (100, 100)

# 粘贴图片 并保存
newCopy.paste(newCopy, (0,0))
newCopy.save('pasted.png')
