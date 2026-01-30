import binascii

hexIv = "391e95a15847cfd95ecee8f7fe7efd66"
cipher = "8473dcb86bc12c6b6087619c00b6657e"
plainText = b"FIRE_NUKES_MELA!"
altering_text  = b"SEND_NUDES_MELA!"

bytesIV = bytes.fromhex(hexIv)

new_IV = ""
for i in range(16):
    A = bytesIV[i] ^ plainText[i] ^ altering_text[i]
    new_IV += chr(A)


new_IV  = new_IV.encode("latin-1").hex()
print(new_IV)

print("flag{"+new_IV+ ",8473dcb86bc12c6b6087619c00b6657e" +"}")