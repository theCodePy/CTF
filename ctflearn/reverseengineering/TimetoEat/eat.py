# I wrote and debugged this code with all the convoluted "int" variable names.
# Was it confusing? Yes. Was debugging hard? Yes.
# Did I spend more time than I should have on this problem? Yes

# int = int
# len = len
# print = print
# str = str
# str.isdigit = str.isdigit

def mul3(eat):
    return str(int(eat)*3)

def EAt(eat, eats):
    print(eat, eats)
    i = 0
    j = 0
    eateat = 0
    eAt = ""
    print(f"i={len(eat)}, j={len(eats)}")
    while i < len(eat) and j < len(eats):
        if eateat%3 == 0:
            eAt += eats[j]
            j += 1
        else:
            eAt += eat[i]
            i += 1
        eateat += 1
    return eAt

def decrypt(eateat):
    eat = ""
    eats = ""
    i = 0
    while i < len(eateat):
        if i%3==0:
            eats += eateat[i]
        else:
            eat += eateat[i]
        i+=1
    print(i, len(eateat))    
    print(eat, eats)
    print("does it worked ",  EAt(eat, eats))
    print("does it worked ", "E10a23t9090t9ae0140")
    print("E10a23t9090t9ae0140" ==  EAt(eat, eats))
    return eat[3:][::-1]


def string_reverse(eat):
    return eat[::-1]

def eaT(eat):
    return mul3(eat[:3]) + string_reverse(eat)

def aTE(eat):
    return eat #*len(eat)

def Ate(eat):
    return "Eat" + str(len(eat)) + eat[:3]

def Eat(eat):
    if len(eat) == 9:
        if str.isdigit(eat[:3]) and\
            str.isdigit(eat[7:]):
                eateat = EAt(mul3(eat[:3]) + string_reverse(eat) , "Eat9" + string_reverse(eat)[:3] )
                if eateat == "E10a23t9090t9ae0140":
                    flag = "eaten_" + eat
                    print("absolutely EATEN!!! CTFlearn{"+flag+"}")
                else:
                    print("thats not the answer. you formatted it fine tho, here's what you got\n>>", eateat)
        else:
            print("thats not the answer. bad format :(\
            \n(hint: 123abc456 is an example of good format)")
    else:
        print("thats not the answer. bad length :(")

print("what's the answer")
eat = input()
# length_d_3 = len(eat)//3
# 4 = length_d_3+1
# 2 = length_d_3-1
Eat(eat)
print("flag decrypted: ", decrypt("E10a23t9090t9ae0140"))
# input length should be 9
# length_d_3 = 3