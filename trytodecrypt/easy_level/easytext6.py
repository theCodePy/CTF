import string

cipher = "4D586CFC2DB449D47B0CF99C3BC46CFC7B0C"

word = string.digits + string.ascii_letters +  "-_.,;:?! "


def decrypt(cipher):
    plaintext = ''
    cipher = [cipher[i:i+4] for i in range(0,len(cipher),4)]
    for c in cipher:
        index = int(c,16)//900 -1
        plaintext += word[index]

    return plaintext

print(decrypt(cipher))