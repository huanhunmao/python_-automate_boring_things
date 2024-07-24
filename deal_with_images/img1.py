from PIL import ImageColor, Image

print(ImageColor.getcolor('red', 'RGBA')) # (255, 0, 0, 255)
print(ImageColor.getcolor('RED', 'RGBA')) # (255, 0, 0, 255)

catIm = Image.open('image.png')
print(catIm) # <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=216x202 at 0x100D382B0>
print(catIm.size) # (216, 202)

width, height = catIm.size
print(width, height) # 216 202

print(catIm.format) # PNG
print(catIm.filename) # ... image.png
print(catIm.format_description) # Portable network graphics
