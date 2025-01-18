import string

cipher = "0C02D8010D0C02D8010606D8101402FCD80F0603D8FC0600DA"

word = string.digits + string.ascii_letters + "-_.,;:?! "


def decrypt(cipher):
    plaintext = ""
    cipher = [ cipher[i:i+2] for i in range(0,len(cipher),2)]
    for c in cipher:
        index = len(word)-1 - ((int(c, 16) - 216) % 256)
        plaintext += word[index]

    return plaintext


print(decrypt(cipher))