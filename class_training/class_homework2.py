#car instance
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0#li cheng biao
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+str(self.make)+' '+str(self.model)
        return long_name
    def read_odometer(self):
        print('this car has '+ str(self.odometer_reading)+' miles on it')
    def update_odometer(self,miles):
        if miles>0:
            self.odometer_reading+=miles
        else:
            print('be honest')
    def fill_gas_tank():
        print("full")

my_new_car=Car('Audi','A4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading=20
my_new_car.read_odometer()
my_new_car.update_odometer(500)
my_new_car.read_odometer()


class ElectricCar(Car):
    def __init__(self,make,model,year,battery_size=70):
        super().__init__(make,model,year)
        self.battery_size=Battery()
    def describe_battery(self):
        print('This Car has a ' + str(50) + '-kwh battery.')#

    def fill_gas_tank(self):
        print("no gas_tank")
class Battery():
    def __init__(self,Battery_size=70):
         self.battery=Battery_size
    def describe_battery(self):
        print('this car has a '+ str(self.battery)+'-KMH battery.')
    def get_range(self):
        range=self.battery*50
        print(f'this car can run {range} miles more!')
    def upgrade_battery(self,Battery):
        self.battery=Battery

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery_size.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery_size.get_range()
my_tesla.battery_size.upgrade_battery(200)
my_tesla.battery_size.get_range()
