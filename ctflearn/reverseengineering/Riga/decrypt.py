import string

printables = string.ascii_letters + string.digits + string.punctuation

pickle2 = [157, 172, 146, 235, 179, 191, 237, 233, 228, 151, 185, 148, 232, 225, 179, 185, 148, 191, 227, 225, 183, 191, 255, 250]

pickle1 = [158,	173, 147, 181, 188, 184, 238, 234, 229, 144, 186, 184, 235, 186, 237, 227, 232, 188, 238, 186, 237, 235, 184, 238, 236, 251]

pickle0 = [159, 174, 156, 182, 189, 185, 239, 235, 230, 158, 185, 236, 179, 185, 227, 185, 187, 168, 137, 227, 189, 239, 187, 150, 185, 237, 227, 137, 185, 228]


def pickle1_decrypt(charM, index):
    if index < 3:
        charM = charM  ^ 222
        charM ^= 0xdededededededede
        charM = charM % 256
    if index==3:
        charM = charM  ^ 222
        charM ^= 0xdede
        charM = charM % 256
    
    c = charM
    b = (charM + 18 ) % 256
    if b < 127:
        if b<32:
            b = (c + 113) % 256
        if b ^ 203 == pickle1[index] :
            return 1
    elif (c + 179 ^ 203) % 256 == pickle1[index]:
        return 1
    
    return 0


def pickle0_decrypt(charM, index):
    
    if index < 3:
        charM = charM  ^ 222
        charM ^= 0xdededededededede
        charM = charM % 256
    elif index==3:
        charM = charM  ^ 222
        charM ^= 0xdededede
        charM = charM % 256
    elif index == 28:
        charM = charM  ^ 222
        charM ^= 0xdede
        charM = charM % 256
        

    c = charM
    b = charM + 17
    if b < 127:
        if b<32:
            b = c + 112
        if (b ^ 203) == pickle0[index] :
            return 1
    elif (c + 178 ^ 203) % 256 == pickle0[index]:
        return 1
    
    return 0



def pickle2_decrypt(charM, index):
    
    if index < 3:
        charM = charM  ^ 222
        charM ^= 0xdededededededede
        charM = charM % 256

    c = charM
    b = charM + 19
    if b < 127:
        if b<32:
            b = c + 114
        if (b ^ 203) % 256 == pickle2[index] :
            return 1
    elif (c + 180 ^ 203) % 256 == pickle2[index]:
        return 1
    
    return 0



flag = ""
for i in range(len(pickle1)):
    for c in printables:
        if pickle1_decrypt(ord(c), i):
            flag += c
            break
    else:
        print("pickle1:index, ", i, "not found")
        flag += '~'
print("pickle1:", flag)


flag = ""
for i in range(len(pickle0)):
    for c in printables:
        if pickle0_decrypt(ord(c), i):
            flag += c
            break
    else:
        print("pickle0:index, ", i, "not found")
        flag += "~"
print("pickle0:", flag)


flag = ""
for i in range(len(pickle2)):
    for c in printables:
        if pickle2_decrypt(ord(c), i):
            flag += c
            break
    else:
        print("pickle2:index, ", i, "not found")
        flag += "~"
print("pickle2:", flag)