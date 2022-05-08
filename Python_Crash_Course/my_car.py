from car import Car, ElectricCar

my_new_car = Car('ford', 'focus', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23_000)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())