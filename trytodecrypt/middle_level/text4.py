import string

char_size = 2
cipher = "261129152E152B"
words = string.digits + string.ascii_letters + ' -_.,;:?!'
encoding = "10121413151716181A19"


def string_to_list(strings, char_size):
    return  [ strings[i:i+char_size] for i in range(0,len(strings),char_size)]


cipher = string_to_list(cipher, char_size)
encodes = string_to_list(encoding, char_size)

plaintext = ""
for i in cipher:
    plaintext += words[encodes.index(i)]

print(plaintext)



