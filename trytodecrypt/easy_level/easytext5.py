import string

cipher = "90DE633F425148DE51546CDE725466DE3F2A6936DE4263CCDEAB362A3372DE39545DDE633F36DE51366F63DE545136D8"

word = string.ascii_letters + string.digits + " -_.,;:?!"

encode = "2A2D303336393C3F4245484B4E5154575A5D606366696C6F7275787B7E8184878A8D909396999C9FA2A5A8ABAEB1B4B7BABDC0C30C0F1215181B1E212427DEC6C9CCCFD2D5D8DB"

plaintext = ""
for i in range(0, len(cipher), 2):
    c = cipher[i:i+2]
    for j in range(0, len(encode), 2):
        if c == encode[j:j+2]:
            plaintext += word[j//2]
            
print(plaintext)