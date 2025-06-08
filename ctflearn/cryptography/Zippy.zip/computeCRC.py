import zlib
import string
from tqdm import tqdm

crc = [ 0x21776b53, 0xd3aa2e11, 0x2788059e, 0x657c5288, 0xfc366b00, 0x0315da00, 0xf1cfb997, 0xfc6b5b86, 0x3cc92888, 0xa6e14c90, 0x5cf6c887, 0xfc98a835, 0xea80990c ]

printable = string.printable

flag_parts = ['']*13
parts_found = 0
for f in tqdm(printable):
    for l in printable:
        for a in printable:
            for g in printable:
                flag = f+l+a+g
                checksum = zlib.crc32(flag.encode())
                if checksum in crc:
                    flag_parts[ crc.index(checksum) ] = flag
                    parts_found +=1

print("toatal parts found ", parts_found)
print("flag : ", ''.join(flag_parts))

# a = zlib.crc32('}'.encode())
# print(a == 0xfcb6e20c)
# print(hex(a))
# print(a)