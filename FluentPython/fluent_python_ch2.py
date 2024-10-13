import bisect
import sys

HAYSTACK = [1,4,5,6,8,12,15,20,21,23,26,29,30]
NEEDLES = [0,1,2,5,8,10,22,23,29,30,31]

[HAYSTACK.insert(bisect.bisect(HAYSTACK, x), x) for x in NEEDLES]
#print(HAYSTACK)

breakpoints = [60,70,80,90]
grades = 'FDCBA'

l = [ grades[bisect.bisect_left(breakpoints, x)] 
     for x in [33,99,77,70,80,81] ]

print(l)