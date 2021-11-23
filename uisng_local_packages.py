
from car_package import car_module
car = car_module.Car(200,10,10)

import car_package.car_module
car = car_package.car_module.Car(200,10,10)

from car_package.car_module import Car
car = Car(200,20,10)