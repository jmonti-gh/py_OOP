''' 2.4.1.7 Lab – timestamping logger '''
import datetime as dtm

# def timestamp_dec(funct):
#     def inner(*args, **kwargs):
#         # printing timestamp before function
#         print('\n', dtm.datetime.today())
#         # getting the return value
#         rval = funct(*args, **kwargs)
#         print('This is after funct. execution')
#         return rval
#     return inner

# def timestamp_dec(funct):
#     print('\n', dtm.datetime.today())
#     return funct

# def timestamp_dec(funct):
#     def inner(*args, **kwargs):
#         # getting the return value
#         rval = funct(*args, **kwargs)
#         # printing funt ret val + time stamp
#         print('\n', rval, '  - ', dtm.datetime.today())
#     return inner

# def timestamp_dec(funct):
#     def inner(*args, **kwargs):
#         # getting the return value
#         rval = funct(*args, **kwargs)
#         # printing funt ret val + time stamp
#         # return rval
#         print(rval, '  - ', dtm.datetime.today())
#         return ''
#     return inner

def timestamp_dec(funct):
    def inner(*args, **kwargs):
        print('\n', dtm.datetime.today(), sep='')
        return funct(*args, **kwargs)
    return inner

@ timestamp_dec
def add(*args):
    r = 0
    for n in args:
        r += n
    return r

@ timestamp_dec
def mult(*args):
    print('--- mult ---')
    r = 1
    for n in args:
        r *= n
    return r

@ timestamp_dec
def sub(a, b):
    return a - b

print(sub(10, 2))
print(add(10, 2))
print(add(2, 1, 4))
print(mult(3, 1, 1, 2, 10))