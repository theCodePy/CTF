
lines = open("data.dat", 'r').readlines()

zero = 0
one = 0
matches = 0
for i in lines:
    i = i.strip()
    zero = i.count("0")
    one = i.count('1')
    if zero%3==0 or one%2==0:
        matches += 1

    zero = 0
    one = 0

print(matches)

