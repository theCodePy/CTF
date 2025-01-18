import string

char_size = 2
cipher = "21052F151200271512413E35101A152F3511"
words = string.digits + string.ascii_letters + ' -_.,;:?!'
encoding = "2A1B43172B012E093339270B41450E1011052F1C161804353E371D1F15211A23000C3B301E13253C292C31220D0F34383A3D02082D362432200A063F1914124026034207442846"


def string_to_list(strings, char_size):
    return  [ strings[i:i+char_size] for i in range(0,len(strings),char_size)]


cipher = string_to_list(cipher, char_size)
encodes = string_to_list(encoding, char_size)

plaintext = ""
for i in cipher:
    plaintext += words[encodes.index(i)]

print(plaintext)



