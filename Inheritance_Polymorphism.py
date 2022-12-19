''' 2.2.1.8/9 Inheritance and polymorphism — two pillars of OOP combined '''

class Device:
    def turn_on(self):
        print('The device was turned on')
# Inheritance: class Radio inherits the turn_on() method from its superclass
class Radio(Device):
    pass

# polymorphism: all class instances allow the calling of the turn_on() method,
#  even when you refer to the objects using the arbitrary variable element
class PortableRadio(Device):
    def turn_on(self):
        print('PortableRadio type object was turned on')

class TvSet(Device):
    def turn_on(self):
        print('TvSet type object was turned on')

device = Device()
radio = Radio()
portableRadio = PortableRadio()
tvset = TvSet()

for element in (device, radio, portableRadio, tvset):
    element.turn_on()

### Duck Typing
print()
class Wax:
    def melt(self):
        print("Wax can be used to form a tool")

class Cheese:
    def melt(self):
        print("Cheese can be eaten")

class Wood:
    def fire(self):
        print("A fire has been started!")

for element in Wax(), Cheese(), Wood():
    try:
        element.melt()
    except AttributeError:
        print('No melt() method')

''' polymorphism is used when different class objects share conceptually similar
 methods (but are not always inherited)
polymorphism leverages clarity and expressiveness of the application design 
and development;
when polymorphism is assumed, it is wise to handle exceptions that could pop
 up.'''
