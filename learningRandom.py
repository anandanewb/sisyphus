import random

random_ints = [random.randint(0,1000) for _ in range(10)]
print(random_ints)

random_floats = [random.random() for _ in range(10)]
print(random_floats)

random_floats2 = [random.uniform(0,100) for _ in range(10)]
print(random_floats2)

print(random.sample(random_ints, 3))

string = "GeeksforGeeks"
print("with string: ", random.sample(string, 4))