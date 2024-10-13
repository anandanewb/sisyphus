class Repeater:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


class MyRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats 
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

#For python 2.0 backward compatibility
    def next(self):
        return self.__next__()

even_squares = (x ** 2 for x in range(10) if x % 2 == 0)

#iterator chains

int_gen = (x for x in range(10))

def integers():
    for i in range(1,10):
        yield i

def squared(seq):
    for i in seq:
        yield i**2 

def negated(seq):
    for i in seq:
        yield -i

negated_squares = negated(squared(integers()))

name_for_userid = {
    382: 'Alice',
    590: 'Bob',
    951: 'Dilbert',

}

def greeting(uid):
    return f'Hi {name_for_userid.get(uid, "there")}'