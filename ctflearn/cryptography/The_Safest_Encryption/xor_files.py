
file1 = open("CTFLearn.pdf", 'rb').read()
file2 = open("CTFLearn.txt", 'rb').read()
file3 = open("xored2file.pdf", 'wb')

for i in range(len(file1)):
    x = file1[i] ^ file2[i]
    file3.write(bytes([x]))

file3.close()