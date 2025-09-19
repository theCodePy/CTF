import sys

sys.set_int_max_str_digits(10000)

flag = open("super_encrypted", 'r').readlines()
flag = [int(i.strip()) for i in flag]
k = len(flag)

rev_op = {
    "sub": "+",
    "csub": "+",
    "chsub": "+",
    "chxor": '^',
    "cxor": '^',
    "xor": '^',
    "mul": "//",
    "cmul": '//',
    "chmul": '//',
    "add": "-",
    "cadd": '-',
    "chadd": '-'
}

mucho_encrypto = open("mucho_encrypto.py", 'r').readlines()

def get_func_index(name):
    try:
        ind = mucho_encrypto.index(f"def {name}(x):\n")
    except:
        print(f"def {name} not found")
        quit()
    if mucho_encrypto[ind+1].strip().startswith('#'):
        ind += 1
    return ind + 1


def reverse_most_of_it(flag, name):
    # sub, chsub, csub, chxor, xor, cxor, add, chadd, cadd,  mul, cmul, chmul
    ind = get_func_index(name)
    returner = None
    if mucho_encrypto[ind].strip().startswith('return'):
        returner = 1
        y = int(mucho_encrypto[ind].strip().split(' ')[3])
    else:
        returner = 0
        y = eval(mucho_encrypto[ind].strip().split('=')[1].strip())
    
    op = name.split('_')[0]
    
    if returner == 1:
        return [eval(f"flag[i] {rev_op[op]} y") for i in range(k)]
    elif returner==0:
        return [eval(f"flag[i] {rev_op[op]} y[i]") for i in range(k)] 



def shuffle_reverse(flag, name):
    ind = get_func_index(name)
    shuffler = eval(mucho_encrypto[ind].strip().split('in')[1][:-1].strip())
    return [flag[shuffler.index(i)] for i in range(k)]

def digsub_reverse(flag, name):
    ind = get_func_index(name)
    digger = eval(mucho_encrypto[ind].strip().split('.join(')[1].split("[int(p)]")[0].strip())
    return [int(str(n)[:1] + ''.join([str(digger.index(p)) for p in str(n)[1:]])) for n in flag]

def chunk_reverse(flag, name):
    ind = get_func_index(name)
    y = int(mucho_encrypto[ind].strip().split("[")[1].split(':')[0].strip())
    return flag[k-y:] + flag[:k-y]


flag_enc_ind = 39900
while mucho_encrypto[flag_enc_ind].strip():
    name = mucho_encrypto[flag_enc_ind].strip().split(' ')[2].split('(')[0].strip()
    if name.startswith('digsub'):
        flag = digsub_reverse(flag, name)
    elif name.startswith('shuffle'):
        flag = shuffle_reverse(flag, name)
    elif name.startswith('chunk'):
        flag = chunk_reverse(flag, name)
    else:
        flag = reverse_most_of_it(flag, name)
    flag_enc_ind-=1


flag = ''.join([chr(i) for i in flag])
print("the super secret was encrypted with")
print("40 thousand lines of Horror!!")
print("yet I successfully reverse it")
print("Decrypted message: ", flag)
