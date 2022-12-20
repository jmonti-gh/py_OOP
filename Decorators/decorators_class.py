''' Decorating functions with classes: a decorator does not have to be a function.
In Python, it could be a class that plays the role of a decorator as a function.
classes bring all the subsidiarity they can offer, like inheritance and the ability
 to create dedicated supportive methods.'''

# jm use
___________________________________________________________________________ = print

# We can define a decorator as a class, and in order to do that,
# we have to use a __call__ special class method
class SimpleDecorator:
    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print('"{}" was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        self.func(*args, **kwargs)
        print('Decorator is still operating')

@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('a', 'b', exec='yes')
___________________________________________________________________________()

# Decorators w/ arguments
class WarehouseDecorator:
    def __init__(self, material):
        self.material = material

    def __call__(self, own_function):
        def internal_wrapper(*args, **kwargs):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(
                own_function.__name__, self.material))
            own_function(*args, **kwargs)
            print()
        return internal_wrapper

@WarehouseDecorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)

@WarehouseDecorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@WarehouseDecorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)

pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
___________________________________________________________________________()

# Class decorators (docrating classes)
''' Like function decorators, the new (decorated) class is available under the name 
'MyClass' and is used to create an instance. The original class named 'MyClass' is no
longer available in your name space. The callable object returned by the class decorator
creates and returns a new instance of the original class, extended in some way.'''

def object_counter(class_):
    class_.__getattr__orig = class_.__getattribute__

    def new_getattr(self, name):
        if name == 'mileage':
            print('We noticed that the mileage attribute was read')
        return class_.__getattr__orig(self, name)

    class_.__getattribute__ = new_getattr
    return class_

@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

car = Car('ABC123')
print('The mileage is', car.mileage)
print('The VIN is', car.VIN)

''' Decorators allow us to wrap another callable object in order to extend its behavior.
Decorators rely heavily on closures and *args and **kwargs.
The idea of decorators was described in two documents – PEP 318 and PEP 3129. Don't be
discouraged that the first PEP was prepared for Python 2, because what matters here is
the idea, not the implementation in a specific Python.'''