import string

cipher = "4A3E374A4973483F3D3E4A"

word = string.digits + string.ascii_letters + "-_.,;:?! "

def decrypt(cipher):
    plaintext=""
    cipher = [ cipher[i:i+2] for i in range(0,len(cipher),2)]
    for c in cipher:
        plaintext+=word[(int(c,16)-45)]
    return plaintext

print(decrypt(cipher))