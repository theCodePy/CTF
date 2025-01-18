import string

cipher = "131017171A48221A1D170F"

word = string.digits + string.ascii_letters + "-_.,;:?! "

def decrypt(cipher):
    plaintext=""
    cipher = [ cipher[i:i+2] for i in range(0,len(cipher),2)]
    for c in cipher:
        plaintext+=word[(int(c,16)-2)]
    return plaintext

print(decrypt(cipher))