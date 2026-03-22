
def func2(c1, c2):
    tmp1 = c2
    tmp2 = c1
    return tmp1 ^ tmp2

def func():
    fp = open('flag.txt', 'r').read()
    cipher = ''
    for i in range(len(fp)):
        temp = func2(ord(fp[i]), 170)
        cipher += chr(func2(temp, i))
    print(cipher)
    with open("encrypted_flag.txt", 'w') as f:
        f.write(cipher)
    return None



def decryptor(cipher):
    flag = ""
    for i in range(len(cipher)):
        m = ord(cipher[i]) ^ i ^ 170
        flag += chr(m)
    return flag

cipher = "éÿîÅËÎÞÃÙóÙÕÎÈÊúèÞÎÜÌÌÕÓÕìùÂéçÆÐþÿñÖËîÿôÿ"
print(decryptor(cipher))