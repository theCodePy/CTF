letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(plaintext):
    cipher = ""
    for p in plaintext:
        i = letters.index(p)
        y = (21*i+11)%26
        # print(f"p={p} i={i}  {(21*i+11)} y={y} ")
        # print(f"{(1*i+11)}   {(1*i+11)%26} p={letters[(1*i+11)%26]}")
        cipher += letters[y]
    return cipher

def decrypt(cipher):
    plaintext = ""
    for c in cipher:
        i = letters.index(c)
        x = (5*i+23)%26
        plaintext += letters[x]
    return plaintext

def decrypt_brut(cipher, plaintext):
    for b in range(1,26):
        for a in range(1,50):
            pt = ""
            for c in cipher:
                i = letters.index(c)
                x = (a*i+b)%26
                pt += letters[x]
            if pt == plaintext:
                return f"a={a}, b={b}, {pt}"


print(encrypt("GOOGLE"))
"HTTHIR"
print(decrypt("GELKT"))
print(decrypt_brut("ETCLYDLSX", "ROHANMAJI"))