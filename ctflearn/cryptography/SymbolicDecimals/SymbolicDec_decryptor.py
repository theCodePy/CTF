

cipher = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"

symTable = ")!@#$%^&*("


Decimal = ""
for c in cipher:
    if c not in symTable:
        Decimal += c 
    else:
        Decimal += str(symTable.index(c))

message = ""
for dec in Decimal.split(','):
    message += chr(int(dec))
print(message)