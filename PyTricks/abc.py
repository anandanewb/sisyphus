""" class Base:
    def foo(self):
        raise NotImplementedError()
    
    def bar(self):
        raise NotImplementedError()
    
class Concrete(Base):
    def foo(self):
        return 'foo() called'

# b = Base()
# b.foo() 

c = Concrete()
c.foo()
c.bar() """

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

    def bar(self):
        pass

assert issubclass(Concrete, Base)
c = Concrete()

