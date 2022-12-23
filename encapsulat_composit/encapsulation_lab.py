''' Encapsulation: 2.7.1.5 LAB'''

class AccountError(Exception):
    pass

class BankAccount:
    def __init__(self, number):
        self.__number = number
        self.__balance = 0

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, val=0):
        raise AccountError('Not possible to change the Account Number')

    @number.deleter
    def number(self):
        if self.__balance > 0:
            print('Is not posible to delete an account with positive balance')
        else:
            self.__number = None

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount > 100_000:
            print('Auditing purpouse: fill prev_mony_lndry form')
            self.__balance = amount
        elif amount >= 0:
            self.__balance = amount
        elif amount < 0:
            raise AccountError('Not possible to set negative balance')

    @balance.deleter
    def balance(self):
        if self.__balance > 0:
            print('Is not posible to delete an account with positive balance')
        else:
            self.__balance = None

# Instantiate the class. ba123 obj. w/number 123 and empty balance
print()
ba123 = BankAccount(123)
#print(ba123.__dict__)
print('B.Acc {} - Current Balance: {:>7}'.format(ba123.number, ba123.balance))

# setting the balance to 1000
print()
ba123.balance = 1000
#print(ba123.__dict__)
print('B.Acc {} - Current Balance: {:>7}'.format(ba123.number, ba123.balance))

# trying to set the balance to -200;
print()
try:
    ba123.balance = -200
except AccountError as e:
    print('Result:', e)
print('B.Acc {} - Current Balance: {:>7}'.format(ba123.number, ba123.balance))

# trying to set a new value for the account number;
print()
try:
    ba123.number = 124
except AccountError as e:
    print('Result:', e)
print('B.Acc {} - Current Balance: {:>7}'.format(ba123.number, ba123.balance))

# trying to deposit 1.000.000;
print()
ba123.balance += 1_000_000
#print(ba123.__dict__)
print('B.Acc {} - Current Balance: {:>7}'.format(ba123.number, ba123.balance))

# trying to delete the account attribute containing a non-zero balance.
print()
try:
    del ba123.number
except AccountError as e:
    print('Trying delete account nro:', ba123.number, 'result:', e)
finally:
    print('B.Acc {} - Current Balance: {:>7}'.format(ba123.number, ba123.balance))

# withdraw 1_000
print()
ba123.balance -= 1_000
print('B.Acc {} - Current Balance: {:>7}'.format(ba123.number, ba123.balance))

# empty acc.balance
print()
ba123.balance -= ba123.balance
print('B.Acc {} - Current Balance: {:>7}'.format(ba123.number, ba123.balance))

print()
try:
    del ba123.number
except AccountError as e:
    print('Trying delete account nro:', ba123.number, 'result:', e)
finally:
    print('B.Acc {} - Current Balance: {:>7}'.format(ba123.number, ba123.balance))
    
