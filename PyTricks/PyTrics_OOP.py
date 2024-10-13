class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.color!r}, {self.mileage!r})'
    
#    def __str__(self):
#        return f'a {self.color} car'


my_car = Car('red', 37281)

import copy
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})' 
    
a = Point(23, 42)
b = copy.copy(a)

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                f'{self.bottomright!r})')
    
rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)

#create list of 10 random integers
import random
random.seed(0)
randoms = [random.randint(0, 10) for _ in range(10)]

#create a for loop with index i for iterating over the list
for i, value in enumerate(randoms):
    print(i, value)

