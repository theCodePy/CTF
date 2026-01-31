
encFlag = open("secretMessage.hex", 'rb').read()
formate = "CTFlearn{"

keys = []

for i in range(len(formate)):
    k = encFlag[i] ^ ord(formate[i])
    keys.append(k)

print(keys)
binary_keys = []

for i in range(len(keys)):
    binary_keys.append([])
    for j in range(8):
        binary_keys[i].insert(0, (keys[i] >> j) & 1)

print(binary_keys)
for i in binary_keys:
    print(i)

considering_bits = """
[7, 6, 5, 4, 3, 2, 1, 0]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 1, 0, 1, 1, 0, 1]
"""
xoring_bits = [1,2,4,5,7]
xoring_bitsR = [6,5,3,2,0]

def lfsr(seed):
    msb = 0
    for x in xoring_bitsR:
        msb =  msb ^ ((seed>>x)&1)
    next_key = seed >> 1 | msb << (8 - 1)
    print("next number in lfsr: ", next_key)
    return next_key


seed = 5
print("lfsr started with 5")
message = ""
for f in encFlag:
    M = f ^ seed
    message += chr(M)
    seed = lfsr(seed)

print("Flag: ", message)