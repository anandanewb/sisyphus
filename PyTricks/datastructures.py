import dis

# byte code dissassembly for (23,'a', 'b', 'c')

dis.dis(compile("(23, 'a', 'b', 'c')", '', 'eval'))

dis.dis(compile("[23, 'a', 'b', 'c']", '', 'eval'))

from collections import namedtuple
from sys import getsizeof

point = namedtuple('Point', ['x', 'y', 'z'])

#named tuple for 3 dimensional 
p1 = point(1, 2, 3)
p2 = (1, 2, 3)

getsizeof(p1)

getsizeof(p2)

from typing import NamedTuple
class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool

car1 = Car('red', 3812.4, True)

car2 = Car('red', '3812.4', True)

from struct import Struct

MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)
data
MyStruct.unpack(data)

from types import SimpleNamespace

car1 = SimpleNamespace(color='red', mileage=3812.4, automatic=True)
del car1.automatic
car1.windshield='broken'

