''' 2.3.1.2 Extended function argument syntax 
*args and **kwargs should be put as the last two parameters in a function def.
*args: refers to a tuple of all additional, not explicitly expected pos.l args
**kwargs (keyword arguments) – refers to a dictionary of all unexpected args
that were passed in the form of keyword=value pairs
'''

def combiner_a(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))

combiner_a(10, '20', 40, 60, 30, arg1=50, arg2='66')
# a= 10, b='20', *args=(40,60,30), **kwargs={arg1: 50, arg2:'66}

# Forwarding arguments to other functions
print()
def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs)

def super_combiner(*my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_kwargs', my_kwargs)

combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')

# Pay attention how the super_combiner() function is called
# If we remove the asterisks from the function call
print()
def combiner(a, b, *args, **kwargs):
    super_combiner(args, kwargs)

def super_combiner(*my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_kwargs', my_kwargs)

combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')

# last example shows how to combine *args, a key word, and **kwargs
print()
def combiner(a, b, *args, c=20, **kwargs):
    super_combiner(c, *args, **kwargs)
def super_combiner(my_c, *my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_c:', my_c)
    print('my_kwargs', my_kwargs)
combiner(1, '1', 1, 1, c=2, argument1=1, argument2='1')

