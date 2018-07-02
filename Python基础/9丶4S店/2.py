# Author: wangfang

class CarStore(object):
    def __init__(self):
        self.factory = BwmFactory()
    def order(self,type):
        return self.factory.select_car_type(type)
class BwmFactory(object):
    def select_car_type(self,type):
        if type == "x6":
            return bmw()

class Car(object):
    def move(self):
        print("move...")

class bmw(Car):
    def x6(self):
        pass
    def x5(self):
        pass
car1 =  CarStore()
res1 = car1.order("x6")
res1.move()

car2 = CarStore()
res2 = car2.order("x5")
