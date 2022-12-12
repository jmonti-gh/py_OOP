''' Class: it’s a blueprint or recipe for an instance (so obj.)
Classes describe attributes and functionalities together to
represent an idea as accurately as possible.
There is always one class of any given type '''

class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

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
 traits: 1. variables, info. about the class itself or a class instance
2. methods, behavior that could be applied to the object (formulated as PY functs).'''

# 'dot' notation to address attr. or functs getattr() & setattr
print('drake.weight:', drake.weight)
print("getattr(hen, 'weight'):", getattr(hen, 'weight'))

duckling.weight = 2.8
print("duckling.weight = 2.8 - getattr(duckling, 'weight'):", getattr(duckling, 'weight') )
setattr(hen, 'height', 18)
print("setattr(hen, 'height', 18) - hen.height:", hen.height)

