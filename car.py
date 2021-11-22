class Car:
    speed = 0
    def __init__(self,top_speed, acceleration, brake):
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.brake = brake

    def accelerate(self,lvl=1):
        if (self.speed + (self.acceleration * lvl)) <= self.top_speed:
            self.speed = self.speed + (self.acceleration * lvl)
        else:
            self.speed = self.top_speed
        #self.speed = min((self.speed +(lvl*self.acceleration))
        return self.speed
    def brakes(self,lvl=1):
        if (self.speed - (self.brake * lvl)) >= 0:
            self.speed = self.speed - (self.brake * lvl)
        else:
            self.speed = 0
        return self.speed
    def get_speed(self):
        return self.speed

slow_car = Car(100,20,10)
print(slow_car.get_speed())
slow_car.accelerate()
print(slow_car.get_speed())
slow_car.accelerate(2)
print(slow_car.get_speed())
slow_car.accelerate(2)
print(slow_car.get_speed())
slow_car.accelerate()
slow_car.brakes(1)
print(slow_car.get_speed())
slow_car.brakes()
print(slow_car.get_speed())
slow_car.accelerate(3)
print(slow_car.get_speed())
slow_car.brakes(11)
print(slow_car.get_speed())





