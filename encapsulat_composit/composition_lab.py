''' build a car from a limited set of components. '''

# 
class Vehicle:
    def __init__(self, VIN):
        self.VIN = VIN      # Vehicle Id Number, attrib. available

class Car(Vehicle):
    def __init__(self, VIN, engine, tires):
        super().__init__(VIN)
        self.engine = engine
        self.tires = tires
        print('A new car has been builded')

class Engine:
    def __init__(self, fuel):
        self.fuel = fuel
        self.state = 'just buldid'
    
    def start(self):
        print('Starting {} engine'.format(self.fuel))
        self.state = 'Started'

    def stop(self):
        print('Stoping {} engine'.format(self.fuel))
        self.state = 'Stoped'

    def get_state(self):
        return self.state
        
class Tires:
    def __init__(self, size):
        self.size = size
        self.preasure = 30
    
    def pump(self, val):
        print('Starting {} engine'.format(self.fuel))
        self.state = 'Started'

    def stop(self):
        print('Stoping {} engine'.format(self.fuel))
        self.state = 'Stoped'

    def get_state(self):
        return self.state

# The developer's responsibility is to provide methods for both engine classes, named
# in the same way (here is thestart() method) to make it work in a polymorphic manner.
class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp gas engine'.format(self.hp))


class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print('Starting {}hp diesel engine'.format(self.hp))

print()

my_car = Car(GasEngine(4))
my_car.engine.start()
my_car.engine = DieselEngine(2)
my_car.engine.start()


class Connection:
    def __init__(self, speed):
        self.speed = speed

    def download(self):
        print('Downloading at {}'.format(self.speed))


class DialUp(Connection):
    def __init__(self):
        super().__init__('9600bit/s')

    def download(self):
        print('Dialling the access number ... '.ljust(40), end='')
        super().download()


class ADSL(Connection):
    def __init__(self):
        super().__init__('2Mbit/s')

    def download(self):
        print('Waking up modem  ... '.ljust(40), end='')
        super().download()


class Ethernet(Connection):
    def __init__(self):
        super().__init__('10Mbit/s')

    def download(self):
        print('Constantly connected... '.ljust(40), end='')
        super().download()

print()

# I started my IT adventure with an old-school dial up connection
my_computer = Personal_Computer('1995', DialUp())
my_computer.connection.download()

# then it came year 1999 with ADSL
my_computer.connection = ADSL()
my_computer.connection.download()

# finally I upgraded to Ethernet
my_computer.connection = Ethernet()
my_computer.connection.download()
