''' 2.6.1.3 Abstract classes vs. method overriding '''

# Typical class that can be instantiated
class Recipie:
    def hello(self):
        print('Nothing is blue unless you need it')

bp = Recipie()
print()
bp.hello()


# Python has come up with a module which provides the helper class for defining
# Abstract Base Classes (ABC) and that module name is abc.
import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')

gf = GreenField()
print()
gf.hello()

# Now we'll try to instantiate the BluePrint class:
# bp = BluePrint()    # TypeError: Can't instantiate abst. class BluePrint with abst. meth. hello

# Now we'll try to inherit the abstract class and forget about overriding the abstract method
# by creating a RedField class that does not override the hello method.

class RedField(BluePrint):
    def yellow(self):
        pass

# rf = RedField() # TypeError: Can't instantiate abst. class RedField with abst. method hello