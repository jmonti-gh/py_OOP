'''2.2.1.6 Multiple inheritance — the LAB'''

class Scanner:
    def scan(self):
        print('.scan() method from Scanner class')

class Printer:
    def print(self):
        print('.print() method from Printer class')

class Fax:
    def send(self):
        print('.send() method from Fax class')

    def print(self):
        print('.print() method from Fax class')

class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass


spfo = MFD_SPF()
sfpo = MFD_SFP()

spfo.scan()
spfo.print()
spfo.send()
print()
sfpo.scan()
sfpo.print()
sfpo.send()

''' sfpo never use .print() from Printer class, then define:
class MFD_SFP(Scanner, Fax) will act in the same way'''



