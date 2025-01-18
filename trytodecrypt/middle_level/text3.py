import string
import time


char_size = 3
cipher = "6224F12C1C3FAA5AA54836B3C446D6415E74"
words = string.digits + string.ascii_letters + ' -_.,;:?!'
encoding = "0912C14F1622852A82CB2EE20232534836B38E3A14C44E740B42E4415645875AA5CD5E060462764A66D6807A37C67E970D7208438668898AC8CF8E290692994C96F982AA5AC8AEBA0FA22B45B68B8BBAEBC1CE4C08C2BC4EC61D84DA7DC3FCADEDD01E24E47E6AE8DEA0F"


def string_to_list(strings, char_size):
    return  [ strings[i:i+char_size] for i in range(0,len(strings),char_size)]


cipher = string_to_list(cipher, char_size)[-1::-1]
encodes = string_to_list(encoding, char_size)

plaintext = ""
for i in cipher:
    plaintext += words[encodes.index(i)]
    time.sleep(0.2)
    print(plaintext, end='\r')

print(plaintext)



