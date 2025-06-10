from tqdm import tqdm


multiple_of  = 123457
card_number_found = 5432100000001234

def luhn_algorithm(number):
    num = str(number)
    product = []
    pattern = 2
    for i in num:
        p = int(i) * pattern
        if p!=0 and p>=10:
            p = (p%10) + (p//10)
        product.append(p)
        if pattern==2:
            pattern = 1
        elif pattern ==1:
            pattern = 2
    sum_p = 0
    for p in product:
        sum_p += p 
    if sum_p % 10 == 0:
        return True
    else:
        return False

for num in range(1000000):
    num *= 10000
    card_number = card_number_found + num
    if card_number % multiple_of != 0:
        continue
    if card_number % multiple_of == 0 and luhn_algorithm(card_number):
        print(f"found fraud credit card : {card_number}")
        print("flag : CTFlearn{"+ str(card_number)+"}")
