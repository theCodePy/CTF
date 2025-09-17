
lawn = r"""\|*/|_|.-_\\|.|_.-//
/-\_.--.|-_._\.-|/*-
\\-|..-*-/__*--/.\*-
_/\|.*.---___***_/\.
_-|.\\././_/|.-|_\//
_-*.\..**/|/**.\_./-
|-*|*.-_-////.|**-|-
*\|*_-|_\-|__\_.*.-|
.*///*.*/*\_-\..*-**
*/_\-\.//--/||\\/_|_
*.**/--/**///./\\/-|
/|.\-..*-./\..-|\.||
|\/\__|./*_-\|-/_*_\
.|///*-/\-/|*/*||*-*
.\.|\/.*/--*.|\--\/\
/_/|_|_---\_\_.***.-
|-.._.-*\|*_\/_|_\/*
.\.|\|//_-|.*-*|\*|*
_\/-|-_*\-\|-/-/-*.-
-_..\_\_*\\-*__..*/-"""


lawn = lawn.strip()
lawn = lawn.replace('.', '0').replace('_', '1').replace('\\', '2').replace('-', '3').replace('/', '4').replace('|', '5').replace('*', '6')
# lawn = lawn.split('\n')

lawn = lawn.split('\n')
for i in range(len(lawn)):
    lawn[i] = list(lawn[i])

mowing_pattern = []
# mowing formation
tiles = 0
row = 0
for col in range(len(lawn)):
    for i in range(len(lawn[0])):
        if col%2==0:
            mowing_pattern.append(int(lawn[row][col]))
            row +=1
        if col%2==1:
            mowing_pattern.append(int(lawn[row][col]))
            row -=1
    if col%2==0:
        row-=1
    else:
        row+=1

lawn = mowing_pattern
speed = int(len(lawn)**0.5)
# lawn = list(lawn)
# for i in range(len(lawn)):
#     lawn[i] = int(lawn[i])

# mower = 0
rowEO = 0
tiles = 0
# print("initial state: ", lawn)
for mower in range(len(lawn)):
    if lawn[mower] == 1:
        lawn[mower] = 0
    elif lawn[mower] !=0:
        lawn[mower] -= 2
    grow = mower - speed
    while grow >= 0 :
        if lawn[grow] != 6 and lawn[grow]!=0:
            lawn[grow] += 1
        grow -= speed
    # print(lawn)

print("total numer of flower bloomed: ", lawn.count(6))
        


# lawn = lawn.split('\n')
# for i in range(len(lawn)):
#     lawn[i] = list(lawn[i])
