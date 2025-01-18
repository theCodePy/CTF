import string

cipher = "0A0B1339150B1139070A0B13390510"
# cipher = "F2F3F4F5F6F7F8F9FAFBFCFDFEFF000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F202122232425262728292A2B2C2D2E2F303132343536373839"
# cipher = 'FCFDFE000102030405060708090A0B0C0D0E0F10111213141516'

word = string.digits + string.ascii_letters + "-_.,;:?! "


def decrypt(cipher):
    plaintext=""
    cipher = [ cipher[i:i+2] for i in range(0,len(cipher),2)]
    for c in cipher:
        try:
            plaintext+=word[(int(c,16)-242)%255]
        except:
            print(f"{c} is problematic (int(c,16)={int(c,16)}-242={(int(c,16)-242)} %256={(int(c,16)-242)%256}")
    return plaintext


def encrypt(plaintext):
    cipher = ""
    for p in plaintext:
        c = hex((word.find(p)+242 )%255).replace('0x','')
        if len(c)==1:
            c = '0'+c
        cipher+=c
    return cipher.upper()


# e = encrypt(string.ascii_lowercase)
# print(e)
# print(cipher)
# if e == cipher:
#     print("encrypted correctly")
# else:
#     print("they are not equal you son of a bitch !!")
print(decrypt(cipher))