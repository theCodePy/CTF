
# header2 = "\xff\xd8\xff\xe0"
# header3= "\xff\xd8\xff"
header= "\xff\xd8\xff\xe0\x00\x10\x4a\x46\x49\x46\x00\x01"
# header5="\xff\xd8\xff\xe0\x00\x10\x4a\x46\x49\x46"
header3="\xff\xd8\xff\xe0\x00\x10\x4a\x46"
header2="\xff\xd8\xff\xe0\x00\x10"
footer = "\xff\xd9"
print(len(header))
with open("my_magic_bytes.jpg.enc", 'rb') as file:
    jpg = file.read()

print("length of jpg is :",len(jpg))
index =0
key = []
for i in header:
    k = jpg[index] ^ ord(i)
    key.append(k)
    index+=1
print(key)

index =-2
footerkey = []
for i in footer:
    k = jpg[index] ^ ord(i)
    footerkey.append(k)
    index+=1
print(footerkey)

xored = []
index = 0
k = len(key)
for j in jpg:
    c = j ^ key[index % k]
    xored.append(c)
    index+=1
print("xored header : ", xored[:len(header)])
print(xored[-2:])
if xored[-2:]!=[255,217]:
    print("footer is wrong !!")
    quit()
else:
    print("correct footer")

with open("my_magic.jpg", 'wb') as file:
    for i in xored:
        h = hex(i).replace('0x','')
        if len(h)==1:
            h = "0"+h
        file.write(bytes.fromhex(h))

# i = 1
# while i<(len(xored)//2):
#     if xored[:i] == xored[i:i*2]:
#         index = i
#         print("found repetation:",xored[:i])
#     i+=1
# print("rechecking the repetation")
# i = 0
# passed = 0
# while (i+2)*index<len(xored):
#     if xored[i:index*(i+1)] == xored[index*(i+1):index*(i+2)]:
#         passed+=1
#         pass
#     else:
#         print("the key seems wrong")
#     i+=1