

def check_prime(n):
    if n%2==0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True


def find_prime(prime):
    while True:
        if check_prime(prime):
            q = str(prime)
            p = 0
            for i in q:
                p+=int(i)
            if check_prime(p):
                return prime
            else:
                prime+=1
        else:
            prime+=1

prime = find_prime(1000000)
prime2 = find_prime(prime+1)

print(f"prime={prime}, prime2={prime2}\nsolution={str(prime)+str(prime2)}")
