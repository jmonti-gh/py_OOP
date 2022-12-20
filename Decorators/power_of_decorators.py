''' RealPy: The Power of Python Decorators: Python’s decorators allow you
to extend and modify the behavior of a callable  (functions, methods, and 
classes) without permanently modifying the callable itself. 
-  In basic terms, a decorator is a callable that takes a callable as input
and returns another callable'''

# jm use
______________________________________________________________ = print

''' * Functions are objects —they can be assigned to variables and passed to
and returned from other functions
* Functions can be defined inside other functions—and a child function can
capture the parent function’s local state (lexical closures)'''
______________________________________________________________()

# Maybe the simplest decorator
def null_decorator(func):
    return func

# Let's use to decorate (or wrap) another function
def greet():
    return 'Hello!'

greet = null_decorator(greet)
print(greet())
______________________________________________________________()

# Python's @ syntax for decorating a funct. more conveniently
@null_decorator
def greet_1():
    return 'Hello!'

print(greet_1())
______________________________________________________________()

# Decorators Can Modify Behavior: 
# converts the result of the decorated funct. to uppercase letters
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet_2():
    return 'Hello!'

print(greet_2())

______________________________________________________________()

# Unlike null_decorator , our uppercase decorator returns a different
# function object when it decorates a function:
print(greet)
print(null_decorator(greet))
print(uppercase(greet))

print(greet_2())
