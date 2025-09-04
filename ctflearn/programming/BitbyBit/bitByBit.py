import base64


b64_input = input("enter base64: ").strip()

operands = []
operations = []

clear_texts = base64.b64decode(b64_input).decode()
print(clear_texts)
i = 0
while i < len(clear_texts):
    if clear_texts[i].isalpha():
        operands.append(ord(clear_texts[i]) ** 3)
    elif clear_texts[i] == ">":
        operations.append(">>")
        i+=1
    else :
        operations.append(clear_texts[i])
    i+=1

print(operands)
print(operations)
v = operands[0]
for opi in range(len(operations)):
    for opx in range(opi, len(operations)):
        if operations[opx] == '~':
            v = ~v
        elif operations[opx] == "&":
            v = v & operands[opx + 1]
        elif operations[opx] == ">>":
            v = v >> operands[opx + 1]
        elif operations[opx] == "|":
            v = v | operands[opx + 1]
        elif operations[opx] == "^":
            v = v ^ operands[opx + 1]

print(v)