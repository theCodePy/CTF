
cipher = "\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e"

known = "ctflearn{"
key = []
for i in range(len(known)):
    x = ord(cipher[i]) ^ ord(known[i])
    print(x, end=' ')
    key.append(x)


print()
print(ord(cipher[-1]) ^ ord('}'))

for i in key:
    print(chr(i), end='')

print()

key = "jowls"
flag = ""
for i in range(len(cipher)):
    flag += chr(ord(cipher[i]) ^ ord(key[i%len(key)]))
print(flag)