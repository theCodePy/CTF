import base64


degrees = open("sputnik/transmission1.txt", 'r').read()
validity = open("sputnik/transmission3.txt", 'r').read()

binary_degree = {
    "-": "0",
    "/": '0',
    "|": '1',
    "\\": '1'
}

message_bin = ""
for i in range(len(degrees)):
    if validity[i] == "v":
        message_bin += binary_degree[degrees[i]]

print(message_bin)

message = ""
for i in range(0, len(message_bin), 8):
    message += chr(int(message_bin[i:i+8], 2))

print(message)
print("flag: ", base64.b64decode(message.replace('b64:', '')).decode() )