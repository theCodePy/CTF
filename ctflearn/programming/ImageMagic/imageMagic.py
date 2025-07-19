from PIL import Image

img =  Image.open("out copy.jpg")
flag = Image.new("RGB", (304, 92))
flag_pix = flag.load()
pix = img.load()

w, h = img.size

print("size: ", w, h)
p = 0
for i in range(304):
    for j in range(92):
        flag_pix[i, j] = pix[p, 0]
        p+=1

flag.save("flag.jpg")
flag.show()
