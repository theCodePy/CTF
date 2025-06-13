from tqdm import tqdm
from lcm import lcm
import time

time_start = time.time()
modulo = 2**64 -1
number = 212103456793011
equalto = 183057226632645

# convert to binary array for easy access
binary_number = [ int(i) for i in bin(number).replace('0b','')]
binary_equalto = [ int(i) for i in bin(equalto).replace('0b','')]

# make the size of the array to 64 
binary_number = [0] * (64 - len(binary_number)) + binary_number
binary_equalto = [0] * (64 - len(binary_equalto)) + binary_equalto
binary_buffer = [0] * 64
missing_num = ["0"] * 64

def binary_addition(number, buffer, ptr):
    carry = 0
    n_ptr = -1
    while ptr>=0:
        sum_ = buffer[ptr] + number[n_ptr] + carry
        sum_bin = bin(sum_).replace('0b','')
        sum_bin = '0'* (2-len(sum_bin)) + sum_bin
        buffer[ptr] = int( sum_bin[-1] , 2)
        carry = int( sum_bin[0] )
        ptr -= 1
        n_ptr -=1

        


binary_ptr = 63
while binary_ptr >= 0:
    if  binary_buffer[binary_ptr] != binary_equalto[binary_ptr]: 
        missing_num[binary_ptr] = '1'
        binary_addition(binary_number, binary_buffer, binary_ptr)
        binary_ptr -= 1
    else:
        missing_num[binary_ptr] = '0'
        binary_ptr -= 1

if binary_buffer == binary_equalto:
    print("success !!")

missing_number = int(''.join(missing_num), 2)
print(f" missing number is {missing_number}")
print(f" impossible equation solved: {missing_number} * {number} = {equalto}")
print(f"found in {time.time()-time_start}sec..")