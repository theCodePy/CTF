import string

cipher = [152, 162, 152, 145, 162, 167, 150, 172, 153, 162, 145, 170, 141, 162]

key_numbers = "110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051"

key_numbers = key_numbers.split(' ')
key_message = ""
for i in range(len(key_numbers)):
    key_message += chr(int(key_numbers[i], 8))

print(key_message)
maggie_cost = 847.63

key = chr(round(maggie_cost/8)+4)
key = key + key + chr(ord(key)-4)
print(key)

cipher_chr = ""
for c in range(len(cipher)):
    cipher_chr += chr(int(str(cipher[c]), 8))
    cipher[c] = int(str(cipher[c]), 8)
print()
print(cipher)
print(cipher_chr)
print()


# try caesar cipher with key--> nnj
message = ""
for c in range(len(cipher_chr)):
    indc = (string.ascii_lowercase.index(cipher_chr[c]) - string.ascii_lowercase.index(key[c%len(key)]) )% 26
    message += string.ascii_lowercase[indc]
print(message)

flag = "CTFlearn{" + message + "}"
print("flag: ", flag)
# key len 1 xor bruteforce
# for i in range(256):
#     message = ''
#     for c in cipher:
#         C = c ^ i
#         if chr(C) not in string.printable:
#             break
#         message += chr(C)
#     if len(message) == len(cipher):
#         print(message)
