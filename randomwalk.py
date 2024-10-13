import random

def randomwalk_list():
    last, rand = 1, random.random()
    nums = []
    while rand > 0.1:
        if abs(last - rand) >= 0.4:
            last = rand
            nums.append(rand)
        else:
            print('*')
        rand = random.random()
    nums.append(rand)
    return nums

for num in randomwalk_list():
    print(num)

#randomwalk_list_static()

def randomwalk_static(last=[1]):
    rand = random.random() # initial value
    if last[0] < 0.1:
        return None
    while abs(last[0] - rand) < 0.4:
        print('*')
        rand = random.random() # new candidate 
    last[0] = rand

    return rand

num = randomwalk_static()
while num is not None:
    print(num)
    num = randomwalk_static()


def gen():
    yield 1
    yield 2
    yield 3

def randomwalk_generator():
    last, rand = 1, random.random()
    while rand > 0.1:
        print('*')
        