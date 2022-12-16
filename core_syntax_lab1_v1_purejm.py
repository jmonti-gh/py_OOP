''' time interval multiplicationc'''

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
        return (self.__conv_int(self.hs) + ':' + self.__conv_int(self.ms) +
         ':' + self.__conv_int(self.ss))

    def __conv_int(self, val):
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
        hs, ms, ss = self.__conv_hms(self.tiss * itg)
        return TimeInterval(hs, ms, ss)

    def __add__(self, other):
        #res = self.tiss + other.tiss
        hs, ms, ss = self.__conv_hms(self.tiss + other.tiss)
        return TimeInterval(hs, ms, ss)

    def __sub__(self, other):
        hs, ms, ss = self.__conv_hms(self.tiss - other.tiss)
        return TimeInterval(hs, ms, ss)

# Lab test data:
fti = TimeInterval(21, 58, 50)
print(fti)
sti = TimeInterval(1, 45, 22)
print(sti)
print(fti + sti)
print(fti - sti)

# JM -- tests:            
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