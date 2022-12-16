''' time interval multiplicationc'''

class TimeInterval:
    def __init__(self, hs, ms, ss):
        if type(hs) != int or type(ms) != int or type(ss) != int:
            raise TypeError('Arguments must be integers')
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

    def __mul__(self, itg):
        rti = self.tiss * itg
        hs =  rti // 3600
        ms = (rti % 3600) // 60
        ss = (rti % 3600) % 60
        return TimeInterval(hs, ms, ss)
            
ti1 = TimeInterval(15, 25, 3)
print(ti1)

ti2 = TimeInterval(1, 0, 0)
print(ti2)

print(ti2._TimeInterval__conv_ss())
print(ti1.tiss)

print(ti2 * 2)

ti3 = ti1 * 3
print(ti3)

ti3 = ti3 * 2
print(ti3)