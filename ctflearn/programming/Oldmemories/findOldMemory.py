
from PIL import Image


fstImage = Image.open('1.png')
scndImage = Image.open('2.png')
newImage = Image.new('L', (512,512), 0)


for i in range(512):
    for j in range(512):
        pix = fstImage.getpixel((i,j))
        if pix == scndImage.getpixel((i,j)):
            newImage.putpixel((i,j), pix)

newImage.save("flag.png")