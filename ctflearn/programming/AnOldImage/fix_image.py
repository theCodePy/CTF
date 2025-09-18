from PIL import Image
from collections import defaultdict
from itertools import permutations


img = Image.open("old_image.png")
print(img.size)
print(img.mode)
print(img.getpixel((0,0)))
xyrg_table=[]

pixels = img.getdata()
# for i in range(100):
#     print(pixels[i])
red_count = defaultdict(int)
green_count = defaultdict(int)
for x in range(256):
    for y in range(256):
        R, G, B = img.getpixel((x,y))
        red_count[R] += 1
        green_count[G] += 1
        xyrg_table.append([x,y,R,G])

# img.putpixel((100, 100), (0,0,255))
# print(img.getpixel((100,100)))

# print("redcountsminimum: ", min(red_count.values()))
# print("greencountsmin: ", min(green_count.values()))

# new_img = Image.new("RGB",(256,256), (255,255,255))
# new_img.save("white.png")


# new_img = Image.new("RGB",(256,256), (0,0,0))
# new_img.putpixel((x,y), (r,g,0))

xyrg_perm_obj = permutations([0,1,2,3])

for x,y,r,g in xyrg_perm_obj:
    new_img = Image.new("RGB", (256,256), (0,0,0))
    for xyrg in xyrg_table:
        new_img.putpixel((xyrg[x],xyrg[y]), (xyrg[r], xyrg[g], 0))
    new_img.save(f"{x}{y}{r}{g}.png")
    

for i in red_count:
    if red_count[i]!=256:
        print("got you red handed")
for i in green_count:
    if green_count[i]!=256:
        print("count you geen handed")
if len(green_count)!=256:
    print("caught you geen handed in len")
if len(red_count)!=256:
    print("cought you red handed")


print()
# print(len(pixels))
# print(pixels[100])