''' build a car from a limited set of components. '''

class Vehicle:
    def __init__(self, VIN):
        self.VIN = VIN      # Vehicle Id Number, attrib. available

    ''' works this meth here BUT use traits not know directly in this class'''
    # def get_status(self):
    #     print('\nVehicle: {}, details:'.format(self.instance))
    #     print('    VIN:', self.VIN)
    #     print('    Engine fuel:', self.engine.fuel)
    #     print('    Engine state:', self.engine.get_state())
    #     print('    Tires size:', self.tires.size)
    #     print('    Tires preassure:', self.tires.get_preassure())



class Car(Vehicle):
    def __init__(self, VIN, engine, tires, instance):
        super().__init__(VIN)
        self.engine = engine
        self.tires = tires
        self.instance = instance
        #print('A new car has been builded  - Name:', instance, '\tVIN:', VIN)
        print('A new car has been builded  - Name: {:<28} {} {}'.format(instance, 'VIN', VIN))

    ''' To this subclass all the traits used are presented already'''
    def get_status(self):
         print('\n{}: {}.  - Details:'.format(self.__class__.__name__, self.instance))
         print('\tVIN:', self.VIN)
         print('\tEngine fuel:', self.engine.fuel)
         print('\tEngine state:', self.engine.get_state())
         print('\tTires size:', self.tires.size)
         print('\tTires preassure:', self.tires.get_preassure())

class Engine:
    def __init__(self, fuel):
        self.fuel = fuel
        self.__state = 'just ensambled'
    
    def start(self):
        print('Starting {} engine'.format(self.fuel))
        self.__state = 'Started'

    def stop(self):
        print('Stoping {} engine'.format(self.fuel))
        self.__state = 'Stoped'

    def get_state(self):
        return self.__state
        
class Tires:
    def __init__(self, size):
        self.size = size
        self.__preassure = 20
    
    def pump(self, val):
        print("Adding {} units to car's tires".format(val))
        self.__preassure += val

    def get_preassure(self):
        return self.__preassure

city_tires = Tires(15)
off_road_tires = Tires(18)
electric_eng = Engine('electricity')
pertrol_en = Engine('petrol')

city_car = Car('ELE123', electric_eng, city_tires, 'City car')
all_terrain_car = Car('PTL987', pertrol_en, off_road_tires, 'All terrain vehicle')

# # Manual instrospection (first aproach) Check city_car status
# print()
# print('City Car Details:')
# print('  VIN:', city_car.VIN)
# print('  Engine fuel:', city_car.engine.fuel )
# print('  Engine status:', city_car.engine.get_state())

city_car.get_status()
all_terrain_car.get_status()

# Start city car & add 8 lbs to it's tires.
print()
city_car.engine.start()
city_car.tires.pump(8)
# See actual city car status
city_car.get_status()