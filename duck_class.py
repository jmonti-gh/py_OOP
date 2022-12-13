''' Class: it’s a blueprint or recipe for an instance (so obj.)
Classes describe attributes and functionalities together to
represent an idea as accurately as possible.
There is always one class of any given type '''
from time import sleep

class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self, steps):
        for i in range(steps):
            sleep(0.5)
            print('\t' * i, '...', i+1, sep='')
        print()

    def quack(self):
        return print('Quack')
    
''' An instance is one particular physical instantiation of a class
that occupies memory and has data elements.
An object is everything in Python that you can operate on, like a
class, instance, list, or dictionary.
The term instance is very often used interchangeably with the term
object, because object refers to a particular instance of a class.
It’s a bit of a simplification, because the term object is more general
 than instance. '''
    
# The relation between instances and classes is quite simple: we have one
# class of a given type and an unlimited number of instances of a given class.

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")
# Three different instances based on the Duck class
# We haven't called any object attributes.

''' An attribute is a capacious term that can refer to two major kinds of class
 traits: 1. variables, and 2. methods.'''

# 'dot' notation to address attr. or functs getattr() & setattr()
# Variables: information about the class itself or a class instance
print()
print('drake.weight:', drake.weight)
print("getattr(hen, 'weight'):", getattr(hen, 'weight'))

duckling.weight = 2.8
print("duckling.weight = 2.8 - getattr(duckling, 'weight'):", getattr(duckling, 'weight') )
setattr(hen, 'height', 18)
print("setattr(hen, 'height', 18) - hen.height:", hen.height)

# Methods: behavior that could be applied to the object (formulated as PY functs)
print()
drake.quack()
hen.walk(3)

''' A type is one of the most fundamental and abstract terms of Python:
foremost type that a class can inherit; type class is 'type'; type/kind of
any object; type() function; type() w/3 args > new type 'mataclass'. '''

# Information about an object’s class is contained in __class__.
print()
print(Duck.__class__, '  - type(Duck):', type(Duck))
print(duckling.__class__,'  - type(duckling):', type(duckling))
print(duckling.sex.__class__)
print(duckling.quack.__class__)

# A little subclass example
class diving_duck(Duck):
    def dive(self, meters):
        for i in range(meters):
            sleep(0.5)
            print('\t' * (meters//2), 'glu' * i, i+1)
        print()

print()
d_duck = diving_duck(height=20, weight=3.4, sex="female")
print(d_duck.sex)
d_duck.quack()
d_duck.dive(4)

print()
print(diving_duck.__class__, '  - type(diving_duck):', type(diving_duck))
print(d_duck.__class__,'  - type(d_duck):', type(d_duck))