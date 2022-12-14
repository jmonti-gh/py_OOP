''' Another example shows that a class variable of a super class can be used to
count the number of all objects created from the descendant classes (subclasses).
We'll achieve this by calling the superclass __init__ method.'''

class Phone:
    counter = 0

    def __init__(self, number):
        self.number = number
        Phone.counter += 1  # it's run eveerytime subclass run super().__init__(..)

    def call(self, number):
        message = 'Calling {} using own number {}'.format(number, self.number)
        return message


class FixedPhone(Phone):
    last_SN = 0
    counter = 0

    def __init__(self, number):
        super().__init__(number)
        FixedPhone.last_SN += 1
        self.SN = 'FP-{}'.format(FixedPhone.last_SN)
        FixedPhone.counter += 1


class MobilePhone(Phone):
    last_SN = 0
    counter = 0

    def __init__(self, number):
        super().__init__(number)
        MobilePhone.last_SN += 1
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)
        MobilePhone.counter += 1

# Fixed & Mobile SN (self.SN) is an instance var that you build from last_SN class var
# And last_SN class var store the counter of nbr of subclasses objects

print('Total number of phone devices created:', Phone.counter)
print('Creating 2 devices')
fphone = FixedPhone('555-2368')
mphone = MobilePhone('01632-960004')

# Can see serials in objects dicts.
print()
print('fphone.__dict__:', fphone.__dict__)
print('mphone.__dict__:', mphone.__dict__)
print('Total number of phone devices created:', Phone.counter)
print('\tTotal fixed phones:', FixedPhone.counter, ' - Total mobile phones:', MobilePhone.counter)
print()

