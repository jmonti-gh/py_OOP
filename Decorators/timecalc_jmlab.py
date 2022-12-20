''' 2.4.1.7 Lab – timestamping logger '''
import time as tim

def calc_time(func):
    def inner(*args, **kwargs):
        begin = tim.time()
        print(tim.ctime(begin))
        print(func(*args, **kwargs))
        end = tim.time()
        print("Total time taken in : ", func.__name__, end - begin)
        return ''
    return inner

@ calc_time
def add(*args):
    r = 0
    for n in args:
        r += n
    return r

@ calc_time
def mult(*args):
    print('--- mult ---')
    r = 1
    for n in args:
        r *= n
    return r

@ calc_time
def sub(a, b):
    return a - b

print(sub(10, 2))
print(add(10, 2))
print(add(2, 1, 4))
print(mult(3, 1, 1, 2, 10))