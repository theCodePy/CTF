import string

cipher = "90DE633F425148DE51546CDE725466DE3F2A6936DE4263CCDEAB362A3372DE39545DDE633F36DE51366F63DE545136D8"

word = string.digits + string.ascii_letters +  "-_.,;:?! "

def decrypt(cipher):
    plaintext = ""
    cipher = [ cipher[i:i+2] for i in range(0,len(cipher),2)]
    for c in cipher:
        index = (int(c, 16)-11)//3
        plaintext+=word[index]
    return plaintext

print(decrypt(cipher))