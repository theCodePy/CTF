

flagStack = [0]

commands = open("input.txt",'r').read()

for opt in commands:
    if opt=='+':
        flagStack[-1] += 1
    
    if opt == '-':
        flagStack[-1] -= 1
    
    if opt=='>':
        element = flagStack.pop(0)
        flagStack.append(element)
    
    if opt=='<':
        element = flagStack.pop(-1)
        flagStack.insert(0, element)
    
    if opt=='@':
        flagStack[-1], flagStack[-2] = flagStack[-2], flagStack[-1]
    
    if opt=='.':
        flagStack.append(flagStack[-1])
    
    if opt=='€':
        print(flagStack)
        flag_middle = ''.join([chr(i) for i in flagStack])
        print(f"CTFlearn{"{"+flag_middle+'}'}")
    