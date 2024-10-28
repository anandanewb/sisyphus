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

# 4.7 Class vs Interface Variable Pitfalls
class Dog:
    num_legs = 4

    def __init__(self, name):
        self.name = name    
        pass

jack = Dog('Jack')
jill = Dog('Jill')
print(jack.name, jill.name)

class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1

print(CountedObject.num_instances)

for _ in range(0,3):
    print(CountedObject().num_instances)


# 4.8 Instance, Class and Static Methods Demystifiedj
class MyClass:
    def method(self):
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    
    @staticmethod
    def staticmethod():
        return 'static method called'

    
obj = MyClass()

obj.method()
MyClass.method(obj)

MyClass.classmethod()

MyClass.staticmethod()
obj.staticmethod()



import math
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
    
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
    

Pizza(['cheese', 'tomatoes'])

Pizza.margherita()

Pizza.prosciutto()

import math

class Pizza2:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def area(self):
        return self.circle_area(self.radius)
    
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi