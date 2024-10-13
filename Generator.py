#generator

def even_gen():
    result = 0 
    while True:
        yield result
        result += 2


def odd_gen():
    result = 1
    while True:
        yield result
        result += 2

def even_genexp():
    return (num for num in even_gen())

def odd_genexp():
    return (num for num in odd_gen())

class EvenIter:
    def __init__(self):
        self.value = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        next_value = self.value
        self.value += 2
        return next_value
    

def fibonacci_gen():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

fib_gen = fibonacci_gen()

fibonacci_numbers = (fib_gen.send)