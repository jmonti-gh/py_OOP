''' Extend the class implementation prepared in the previous lab to support
the addition & subtraction of integers (seconds) to time interval objects'''

class TimeInterval:
    def __init__(self, hs, ms, ss):
        if type(hs) != int or type(ms) != int or type(ss) != int:
            raise TypeError('Arguments must be integers')
        if ms > 59 or ms < 0:
            raise ValueError('Minutes must be an integer b/0 an 59')
        if ss > 59 or ss < 0:
            raise ValueError('Segunds must be an integer b/0 an 59')
        self.hs = hs
        self.ms = ms
        self.ss = ss
        self.tiss = self.__conv_ss()

    def __str__(self):
        return (self.__conv_str(self.hs) + ':' + self.__conv_str(self.ms) +
         ':' + self.__conv_str(self.ss))

    def __conv_str(self, val):
        if val < 10:
             val = '0' + str(val)
        else:
            val = str(val)
        return val

    def __conv_ss(self):
        hss = self.hs * 3600
        mss = self.ms * 60
        return self.ss + mss + hss

    def __conv_hms(self, val):
        hsi =  val // 3600
        msi = (val% 3600) // 60
        ssi = (val % 3600) % 60
        return hsi, msi, ssi

    def __mul__(self, itg):
        if not isinstance(itg, int) or itg < 0:
            raise ValueError('Second argument must be an integer > 0')
        hs, ms, ss = self.__conv_hms(self.tiss * itg)
        return TimeInterval(hs, ms, ss)

    def __get_term(self, ety):
        if isinstance(ety, int):
            termi= ety
        elif isinstance(ety, TimeInterval):
            termi = ety.tiss
        else:
            raise TypeError('Second argument not valid')
        return termi

    def __add__(self, other):
        term = self.__get_term(other)
        hs, ms, ss = self.__conv_hms(self.tiss + term)
        return TimeInterval(hs, ms, ss)

    def __sub__(self, other):
        term = self.__get_term(other)
        hs, ms, ss = self.__conv_hms(self.tiss - term)
        return TimeInterval(hs, ms, ss)

# Lab test data:
print('-------- Lab1:')
fti = TimeInterval(21, 58, 50)
print(fti)
sti = TimeInterval(1, 45, 22)
print(sti)
print(fti + sti)
print(fti - sti)
print(fti * 2)
print('-------- Lab2:')
tti = TimeInterval(21, 58, 50)
print(tti + 62)
print(tti -62)

# JM -- tests: 
# print()
# print(fti + 2)
# print(fti + 3600)
# print(fti - 2)
# print(fti - 3600)
# 
#            
# ti1 = TimeInterval(15, 25, 3)
# print(ti1)

# ti2 = TimeInterval(1, 0, 0)
# print(ti2)

# print(ti2._TimeInterval__conv_ss())
# print(ti1.tiss)

# print(ti2 * 2)

# ti3 = ti1 * 3
# print(ti3)

# ti3 = ti3 * 2
# print(ti3)

#ti4 = TimeInterval(49, 7.8, 5)
#ti5 = TimeInterval(49, '78', 5)
#ti6 = TimeInterval(49, 78, 5)
#ti7 = TimeInterval(49, 5, -2)