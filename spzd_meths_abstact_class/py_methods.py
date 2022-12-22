''' Different faces of Python methods'''

# jm use
_________________________________________________________________ = print

# Already known instance methods:
class Example:
    def __init__(self, value):
        self.__internal = value

    def get_internal(self):
        return self.__internal

example1 = Example(10)
example2 = Example(99)
print(example1.get_internal())
print(example2.get_internal())
_________________________________________________________________()

''' Specialized methods: The static and class methods
our perception of the Python class concept is extended by two types of specialized methods '''

# Class methods - access to class vars
class Example:
    __internal_counter = 0

    def __init__(self, value):  # an instace method by def. (use self)
        Example.__internal_counter +=1   # reference class var as ClassName.__class_var_name

    @classmethod
    def get_internal(cls):      # class meth, signaled w/@classmethod and 'cls' param
        return '# of objects created: {}'.format(cls.__internal_counter)  # cls.__class_var_name

print(Example.get_internal())

example1 = Example(10)
print(Example.get_internal())

example2 = Example(99)
print(Example.get_internal())
_________________________________________________________________()

# Class methods -  alternative constructor, allow handle additional arguments.
class Car:
    def __init__(self, vin):
        print('Ordinary __init__ was called for', vin)
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand):
        print('Class method was called')
        _car = cls(vin)
        _car.brand = brand
        return _car

car1 = Car('ABCD1234')
car2 = Car.including_brand('DEF567', 'NewBrand')

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)
_________________________________________________________________()

# Static methods
class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban
            
    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False

account_numbers = ['8' * 20, '7' * 4, '2222']

for element in account_numbers:
    if Bank_Account.validate(element):
        print('We can use', element, ' to create a bank account')
    else:
        print('The account number', element, 'is invalid')






