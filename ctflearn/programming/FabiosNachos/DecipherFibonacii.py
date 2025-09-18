import base64
from Crypto.Util.number import long_to_bytes

B = open("base.txt", 'r').read()
decodedB = base64.b64decode(B).decode()
print(decodedB)
print()

nacho = ""
flag = "CTFLearn{}"
flag1 = "CTFlearn{}"
flag2 = "ctflearn{}"
flag3 = "flag{}"
flag4 = "abctf{}"
flag5 = "ctf{}"

decodedB = decodedB.split(' ')
# nacho test
for i in range(len(decodedB)):
    decodedB[i] = int(decodedB[i])

number_dic = {}
a = 1
b = 1
c = a + b
i = 2
m = max(decodedB)
while len(number_dic) != len(set(decodedB)):
    a = b
    b = c
    c = a + b
    i += 1
    if c in decodedB:
        number_dic[c] = i
    elif c > m:
        break


# print(number_dic)
message = ""
mesascii_list = []
for i in decodedB:
    mesascii_list.append(number_dic[i])
    message += chr(number_dic[i])
print(mesascii_list)

print("flag: ", message)

# ceaser cipher applied +1 
caeser = ""
for i in range(len(message)):
    caeser  += chr(ord(message[i]) + 1)

print("add 1 to flag: ", caeser)
