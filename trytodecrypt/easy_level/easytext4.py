import string

cipher = "0C02D8010D0C02D8010606D8101402FCD80F0603D8FC0600DA"

word = string.digits + string.ascii_letters + "-_.,;:?! "

encode = "14131211100F0E0D0C0B0A09080706050403020100FFFEFDFCFBFAF9F8F7F6F5F4F3F2F1F0EFEEEDECEBEAE9E8E7E6E5E4E3E2E11E1D1C1B1A1918171615D8E0DFDEDDDCDBDAD9"

plaintext = ""
for i in range(0, len(cipher), 2):
    c = cipher[i:i+2]
    for j in range(0, len(encode), 2):
        if c == encode[j:j+2]:
            plaintext += word[j//2]
            
print(plaintext)