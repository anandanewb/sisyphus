def getMin(l):
    min = []
    if l is None or []:
        min = None
    elif len(l) == 1:
        min = l[0] 
    else:
        min = l[0]
        for x in l[1:]:
            if x < min:
                min = x
    return min

def getMax(l):
    max = []
    if l is None or []:
        max = None
    elif len(l) == 1:
        max = l[0] 
    else:
        max = l[0]
        for x in l[1:]:
            if x > max:
                max = x
    return max

def getMedian(l):
    if l is None or []:
        return None
    elif len(l) == 1:
        return l[0]
    else:
        l.sort()
        if len(l) % 2 == 0:
            mid2 = len(l)//2
            mid1 = mid2 - 1
            return (l[mid1] + l[mid2])/2
        else:
            return l[len(l)//2]
        
getMedian([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
getMedian([1,2])
getMedian([1,2,3,4,5,6,7])
# Test list of random list of integers
import random
l = random.sample(range(1, 1000), 10)
print(f"Median of {l} is {getMedian(l)}")

          

            
            




print(getMax([1,2,3,4,25,6,7,8,9,10]))
print(getMin([1, 2, 3, -14, 5, 6, 7, 8, 9, 10]))