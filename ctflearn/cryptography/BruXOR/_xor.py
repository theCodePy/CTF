
cipher = "q{vpln'bH_varHuebcrqxetrHOXEj"

plaintext1 = "CTFLearn{"
plaintext2 = "flag{"
plaintext3 = "CTF{"
plaintext4 = "ABCTF{"

print(f"The last character : {ord('}') ^ ord(cipher[-1])}")

def key_checking(key):
    print("key:")
    for i,k in enumerate(key):
        x = ord(cipher[i]) ^ ord(k)
        print(f"{x} ",end=' ')
    print("\n")

key_checking(plaintext1)
key_checking(plaintext2)
key_checking(plaintext3)
key_checking(plaintext4)

#got the flag
for c in cipher:
    print(f"{chr(ord(c)^23)}", end='')
print()