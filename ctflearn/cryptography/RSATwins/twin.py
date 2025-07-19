from sympy import nextprime
from decimal import Decimal, getcontext
import sympy
import math
from Crypto.Util.number import long_to_bytes

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

e = 65537
n = 14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899
c = 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587

getcontext().prec = 2048
decimal_number = Decimal(n)
sqrt_result = decimal_number.sqrt()
sqrt_n = int(sqrt_result)

s2 = sqrt_n * sqrt_n
if s2 < n:
    print("s^2 is less then n")
while s2 < n:
    sqrt_n+=1
    s2 = sqrt_n * sqrt_n
 
s = sqrt_n
t = math.isqrt(s2 - n)
while t*t != (s2 - n):
    s += 1
    s2 = s * s
    t = math.isqrt(s2-n)

p = s + t
q = s - t
if sympy.isprime(p) and sympy.isprime(q) and p*q==n:
    print("waalllaaa !! found it")
print("p = ",p)
print("q = ",q)
print(f"p is prime {sympy.isprime(p)}, q is prime {sympy.isprime(q)}")
print(f"p*q=n : {p*q==n}")

phi_n = (p-1) * (q-1)
d = modinv(e, phi_n)
m = pow(c, d, n)
print("message: ", long_to_bytes(m))

##############  Explanation  #####################
"""
If the RSA modulus n = p * q*, where p and q are close, then finding p and q (factorizing n) can be done relatively efficiently. A good approach is to find a value s such that s2 - n is a perfect square. This leads to finding p and q as solutions to a quadratic equation. 

Elaboration:
1. Understanding the problem:
The RSA algorithm relies on the difficulty of factoring the modulus n. When p and q are close, the difference between their square root √n and either p or q is smaller, making factorization easier.

2. Using the fact that p and q are close:
Let s = ( p + q) / 2 and t = ( p - q) / 2. Note that s is close to √n.
Then, n = p * q* = (s + t) * (s - t) = s2 - t2.
If s is close to √n, then t2 = s2 - n and finding t would lead to p = s + t and q = s - t.
Since p and q are close, t will be a relatively small number. This makes finding t by searching near s efficient.

3. Example:
Suppose n = 3233.
√n ≈ 56.87.
Let s = 57.
s2 - n = 572 - 3233 = 3249 - 3233 = 16, which is a perfect square (42).
Thus, t = 4.
p = s + t = 57 + 4 = 61.
q = s - t = 57 - 4 = 53.
Therefore, 3233 = 53 * 61.

"""