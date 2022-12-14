''' Instance variables: exists when and only when it is explicitly created and
added to an object'''

# The keyword self is used to indicate that this variable is created coherently
# and individually for the instance to make it independent from other instances
# of the same class;

class Demo:
    class_var = 'shared variable'
    def __init__(self, value):
        self.instance_var = value

    def set_nvars(self, factor=1):
        self.nvar0 = 'Created by set_nvars() method'
        self.nvar1 = factor
        self.nvar2 = self.instance_var * factor

### ~~~ Instace Variables ~~~ ###

d1 = Demo(100)
d2 = Demo(200)

print("d1's instance variable is equal to:", d1.instance_var)
print("d2's instance variable is equal to:", d2.instance_var)

# adding instance vars by methods
d1.set_nvars(3)
d2.set_nvars()

# __dict__  all the instance variables
print()
print('d1.__dict__:', d1.__dict__)
print('d2.__dict__:', d2.__dict__)

# AND some MORE instance vars on the fly
d1.other1 = True
d2.other2 = None
d1.other3 = [0x00, 0x01, 0x10, 0x11]
d2.other3 = d1.__dict__

# To see them all again.
print()
print('d1.__dict__:\n', d1.__dict__)
print()
print('d2.__dict__:\n', d2.__dict__)
print()

''' Class variables are defined within the class construction, so these
 variables are available before any class instance is created'''
### ~~~ Class Variables ~~~ ###
print()
print('Demo.class_var:', Demo.class_var)
# like instance_vars, class_vars are shown in tge class's dictionary
print(Demo.__dict__)
# when you want to read the class variable value, you can use a class or class
# instance to access it, but not the obj.__dict__.
print('d1.class_var:', d1.class_var)
print('d2.class_var:', d2.class_var)
print()
print('d1.__dict__:\n', d1.__dict__)
print()

'''When you want to set or change a value of the class variable, you should access it
via the class, but not the class instance, as you can do for reading. 
When you try to set a value for the class variable using the object (a variable
referring to the object or self keyword) but not the class, you are creating an instance
variable that holds the same name as the class variable'''

# both instances allow access to the class variable
print(d1.class_var)
print(d2.class_var)
print('.' * 20)

# d1 object has no instance variable
print('contents of d1:', d1.__dict__)
print('.' * 20)

# d1 object receives an instance variable named 'class_var'
d1.class_var = "I'm messing with the class variable"

# d1 object owns the variable named 'class_var' which holds a different value than the class variable named in the same way
print('contents of d1:', d1.__dict__)
print('d1.class_var:', d1.class_var)
print('.' * 20)

# d2 object variables were not influenced
print('contents of d2:', d2.__dict__)

# d2 object variables were not influenced
print('contents of class variable accessed via d2:', d2.class_var)
print()
