''' 2.4.1.7 Lab – timestamping logger '''
import datetime as dtm

def ts_dec(txt):
    def wrapper(funct):
        def inner(*args):
            print('\n', txt, dtm.datetime.today(), sep='')
            return funct(*args)
        return inner
    return wrapper

@ ts_dec('-addends- ')
def add(*args):
    r = 0
    for n in args:
        r += n
    return r

@ ts_dec('-terms- ')
def mult(*args):
    print('--- mult ---')
    r = 1
    for n in args:
        r *= n
    return r

@ ts_dec('-minuend, sustraend- ')
def sub(a, b):
    return a - b

print(sub(10, 2))
print(add(10, 2))
print(add(2, 1, 4))
print(mult(3, 1, 1, 2, 10))