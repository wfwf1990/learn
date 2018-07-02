# Author: wangfang
class Store(object):
    def select_car(type):
        pass
    def order(self,type):
        return self.select_car(type)

class BydStore(Store):
    def __init__(self):
        self.factory = BydFactory()
    def select_car(self,type):
        return self.factory.select_car_type(type)

class CarStore(Store):
    def __init__(self):
        self.factory = BwmFactory()
    def select_car(self,type):
        return self.factory.select_car_type(type)

class BydFactory(object):
    def select_car_type(self,type):
        if type == "宋":
            return byd()


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
class byd(Car):
    def song(self):
        pass
    def tang(self):
        pass
car1 =  CarStore()
res1 = car1.order("x6")
res1.move()
