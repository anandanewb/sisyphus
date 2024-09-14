from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
with open("floats.bin", 'wb') as fp:
    floats.tofile(fp)
    fp.close()

print(floats[:5])
floats2 = array('d')

with open('floats.bin', 'rb') as fp:
    floats2.fromfile(fp, 10**7)

print(f"floats head: {floats[:5]} len: {len(floats)}")
print(f"floats2 head: {floats2[:5]} len: {len(floats2)}")
print(floats == floats2)