
def suffle( block ):
    suffled_ = [0] * len(block)
    i =0 
    while True:
        if i >= len(block) :
            break
        suffled_[i] = block[i+1]
        i+=2
    i=1
    while True:
        if i >= len(block) :
            break
        suffled_[i] = block[i-1]
        i+=2
    return suffled_

def reverse_suffle( block ):
    suffled_ = [0] * len(block)
    i =0 
    while True:
        if i >= len(block) :
            break
        suffled_[i+1] = block[i]
        i+=2
    i=1
    while True:
        if i >= len(block) :
            break
        suffled_[i-1] = block[i]
        i+=2
    return suffled_




def encrypt(block):
    cipher = []
    key = [1, 3, 3, 7, 222, 173, 190, 239]
    for i in range(len(block)):
        cipher.append(block[i] ^ key[i%8])
    return cipher


encrypted = [0x57, 0x42, 0x4b, 0x45, 0xcc, 0xbb, 0x81, 0xcc, 0x71, 0x7a, 0x71, 0x66, 0xdf, 0xbb, 0x86, 0xcd, 0x64, 0x6f, 0x6e, 0x5c, 0xf2, 0xad, 0x9a, 0xd8, 0x7e, 0x6f]

cipher = reverse_suffle(encrypted)
flag  = encrypt(cipher)

flag_ = [chr(i) for i in flag]

print(flag_)
print(''.join(flag_))

# 87	66	75	69	204	187	129	204 113	122	113	102	223	187	134	205 100	111	110	92	242	173	154	216 126	111

# 0x57	0x42	0x4b	0x45	0xcc	0xbb	0x81	0xcc 0x71	0x7a	0x71	0x66	0xdf	0xbb	0x86	0xcd 0x64	0x6f	0x6e	0x5c	0xf2	0xad	0x9a	0xd8 0x7e	0x6f