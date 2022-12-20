''' magic methods, or special purpose methods: reponsable for the calles funct. or operator'''

# '+' operator __add__() magic method
# '+' of two objects w/ magic method
class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.weight + other.weight


p1 = Person(30, 40, 50)
p2 = Person(35, 45, 55)

print(p1 + p2)

''' The '+' operator is in fact converted to the __add__() method and (other example) the len()
function is converted to the __len__() method. These methods must be delivered by a class (now
 it’s clear why we treat classes as blueprints) to perform the appropriate action.'''

# '+' of two objects wo/ magic method
class Sportsman:
    def __init__(self, weight, age, sport):
        self.weight = weight
        self.age = age
        self.sport = sport

    # def __add__(self, other):
    #     return self.weight + other.weight


s1 = Sportsman(30, 40, 'soccer')
s2 = Sportsman(35, 45, 'soccer')

print(s1 + s2)

''' When you design and implement your own classes and you want to make use of Python core
syntax to operate on those class objects, you can easily achieve this by implementing the
 appropriate magic methods.'''