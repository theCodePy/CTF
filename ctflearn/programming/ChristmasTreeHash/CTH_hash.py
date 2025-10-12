import string


# Example usage:
tree_input = """15	8	20	10	12	17	8	9
3	20	18	4	14	12	3
9	16	11	18	18	16	7	19
14	10	14	1	14	13	2	14
2	15	14	11
16	8	18	20	2	3
20	6	14	18	16	19"""

expected_result = ''



def lchr(val):
    val = int(val)
    return string.ascii_letters[val%26]


def cth_step1(tree_input: str):
    # parse input into list of lists of ints, ignore empty lines
    lines = [list(map(int, line.split())) for line in tree_input.strip().splitlines() if line.strip()]
    roots = lines[0]
    branches = lines[1:]

    def traverse(prefix, depth):
        products = []
        if depth >= len(branches):
            return products
        for val in branches[depth]:
            new = prefix * val
            products.append(new)                # include this parent->child product
            # recurse to include deeper products along this path
            products.extend(traverse(new, depth + 1))
        return products

    all_products = []
    for root in roots:
        products = []
        products.append(root)               # include the root itself
        products.extend(traverse(root, 0))  # include products for all paths under this root
        all_products.append(products)
    return all_products


all_products = cth_step1(tree_input)




def add_And_of16bits(all_products):
    and_16_bits = []
    for trees in all_products:
        a = bin(ord(lchr(trees[3]))) + bin(ord(lchr(trees[0]))) + bin(ord(lchr(trees[1]))) 
        a = int(a.replace('0b','')[-16:], 2)
        b = bin(ord(lchr(trees[-2]))) + bin(ord(lchr(trees[-1]))) + bin(ord(lchr(trees[-4]))) 
        b = int(b.replace('0b','')[:16], 2)
        c = a & b
        and_16_bits.append(str(c))
    
    all_results = []
    for results in and_16_bits:
        i = 0
        sum_ = 0
        while results[i: i+2]:
            sum_ += int(results[i: i+2])
            i+=2
        all_results.append(str(sum_))
    return ''.join(all_results)


def cth_hash_(result):
    result = int(result)
    new_value = str(result - 682335424444623172)
    i = 0
    hash_lowercase = ''    
    while new_value[i: i+2]:
        hash_lowercase += lchr(new_value[i: i+2])
        i+=2
    return hash_lowercase


result = add_And_of16bits(all_products)
hashlower = cth_hash_(result)
if hashlower== expected_result and expected_result!='':
    print("flag is correct")
print(f"flag: CTFlearn{'{'+hashlower+'}'}")
