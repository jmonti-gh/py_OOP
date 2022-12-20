import time as tim

'''
print()
def simple_hello():
    print('Hello from simple function!')
    return 5 + 4

def other_h():
    print('Other_HELLO')
    return 1 + 3

def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function

decorated = simple_decorator(simple_hello)
r = decorated()        # r = 5+4 = 9
decorated = simple_decorator(other_h)
print(decorated())     # without print you don´t see the retunr of funct
print(r)

print('-' * 70)

# Practice use of decorators
print()
def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function

@simple_decorator
def simple_hello():
    print('Hello from simple function!')
    return 5 + 4

@simple_decorator
def other_h():
    print('Other_HELLO')
    return 1 + 3

print(simple_hello())
tim.sleep(2)
print(other_h())

'''
# Decorators should be universal > A nested funct. (internal_wrapper) could
# reference an obj. (own_function) in its enclosing scope thanks to the closure.
print()
def simple_decorator(own_function):

    def internal_wrapper(*args, **kwargs):
        print('"{}" was called with the following arguments'.format(own_function.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        #own_function(*args, **kwargs)
        res = own_function(*args, **kwargs)
        print('Decorator is still operating')
        return res

    return internal_wrapper

@simple_decorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)
    return 1 + args[0]

r = combiner(2, 'a', 'b', exec='yes')
print('\n', r, '\n')

'''

# Decorators can accept their own attributes
print()
def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('<strong>*</strong> Wrapping items from {}'
            'with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper

@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)

@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)

pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')

# Decorator stacking
print()
def big_container(collective_material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> The whole order would be packed with', collective_material)
            print()
        return internal_wrapper
    return wrapper

def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            our_function(*args)
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
        return internal_wrapper
    return wrapper

@big_container('plain cardboard')
@warehouse_decorator('bubble foil')
def pack_books(*args):
    print("We'll pack books:", args)

@big_container('colourful cardboard')
@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)

@big_container('strong cardboard')
@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)

pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')

'''