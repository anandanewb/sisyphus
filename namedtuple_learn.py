from collections import namedtuple

def custom_divmod(a,b):
    DivMod = namedtuple("DivMod", "quotient remainder")
    return DivMod(*divmod(a,b))


from dataclasses import astuple, dataclass

@dataclass
class Person:
    name: str
    age: int
    height: float
    weight: float
    country: str = "Canada"
    def __iter__(self):
        return iter(astuple(self))
    
for field in Person("Jane", 25, 1.75, 67):
    print(field)

alist = [field for field in Person("Jane", 25, 1.75, 67)]
print(alist)