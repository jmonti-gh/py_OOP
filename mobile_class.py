''' 1.1.1.6 Classes, Instances, Attributes, Methods — the LAB '''

from time import sleep

class Mobile:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return print('mobile phone', self.number, 'is turned on')

    def turn_off(self):
        print('mobile phone is turned off')

    def call(self, number):
        return print('calling', number)

a20 = Mobile('54261-920')
mate10 = Mobile('54261-910')

print()
a20.turn_on()
mate10.turn_on()
a20.call('5411-987')
a20.turn_off()
mate10.turn_off()

# jm tests of returns
print()
ret_ton = a20.turn_on()
print('ret_ton:', ret_ton)      # funct. print?, NOP, None
ret_toff = a20.turn_off()
print('ret_ton:', ret_ton)      # None
