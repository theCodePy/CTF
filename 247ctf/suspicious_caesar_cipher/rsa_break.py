from Crypto.Util.number import getStrongPrime
# from fractions import gcd
# from secret import flag
import string
import time

flag = open("flag.txt",'r').read()

def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)



def get_key(e=65537, bit_length=2048):
    while True:
        p = getStrongPrime(bit_length, e=e)
        q = getStrongPrime(bit_length, e=e)
        if gcd(e, (p - 1) * (q - 1)) == 1:
            print(p, q)
            return e, p * q


def encrypt(e, n, m):
    return [((ord(c) ** e) % n) for c in m]

def known_plain_text_attack(e):
    known_e = 65537
    known_n=909193180607169730928877645070327819694835874221183905239040600481564219496549170740715570321436648643296246577952530286445740811442175031150028203416010713127103183498015199963759060238668656562720245807131329434079860576914658919174542075897267434002194063938817495166690183839716179931129989707243225404059652125828619458523804338365481266829617406113698464217454261869972176582579989894506031054440321852753937600016678878596616927187914667226552238638031488411721806248408207245248542695890589529869734309934242896420270694938788477235151932477889703431606380573812928152596950891842981642861107885015968996631347538231200342275616015690462707386275456287049772277637379506267328445476462602084580773678764228642899139375838305130296491033084515157991707314550889377168974635766650154742311745382594642876222152370428317408079084865464529882165022460841825970826389862781916931282916191168479883017819972965377708926502480683223905790013483385403867582120263945023227849829704497515605576966672801162159615614637324218488210304744171838935349623532180093004354230433944121745381226806673877370240135191388197823001332319702414887208929984475410680666613500085415193385214447737400673402522441649057510877207502203912638566995909

    plain_text=""
    word = string.ascii_lowercase+ "CTF" + string.digits + "{}"

    file = open("suspicious_caesar_cipher.out", 'r')
    cipher = file.read()
    cipher = cipher.split("Encrypted flag:")[1].strip()
    # cipher = eval(cipher)
    cipher=cipher.replace('[','').replace(']','').strip()
    cipher = cipher.split(',')
    cipher_list = []
    for c in cipher:
        c = c.strip().replace(' ', '').replace('L','')
        if c.strip()!='':
            cipher_list.append(int(c.strip()))
    cipher = cipher_list

    # print(cipher[0])
    # known plain text matches the cipher text it's time to bruteforce
    # index=0
    # for p in plain_text:
    #     if ((ord(p)**known_e)%known_n)!=cipher[index]:
    #         print("what the hell bro")
    #     else:
    #         print("known plaintext attack worked this time!!!")
    #     index+=1

    start = time.time()
    for c in cipher:
        for w in word:
            print(plain_text+w,end='\r')
            if ((ord(w)**known_e)%known_n)==c:
                plain_text+=w
                break
    
    print("\n")
    print("RSA CRACKED !!!!!")
    print(f"time taken {int(time.time()-start)}sec..")
    print("got the FLAG with brute forcing :")
    print(plain_text)
            



known_plain_text_attack(e=65537)


# e, n = get_key()

# print("Generated key:")
# print(e)
# print(n)

# print("Encrypted flag:")
# print(encrypt(e, n, flag))
