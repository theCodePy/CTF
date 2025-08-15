from PIL import Image

_images_ = {}

for i in range(500):
    _images_[i] = Image.open(f"{i}.png")

print(_images_[0].mode)
print(_images_[0].size)


restored = Image.new("RGBA", (500,500))

for y in range(500):
    for x in range(500):
        restored.putpixel((x,y), _images_[y].getpixel((x,0)))
    
restored.save("restored.png")


flag="66 6c 61 67 7b 74 68 33 5f 4b 47 42 5f 6c 30 76 33 73 5f 43 54 46 7d"
flag = flag.split(' ')
print(''.join([chr(int(i, 16)) for i in flag]))