# Author: wangfang

class CarStore(object):
    def order(self,new_money):
        if new_money >50000:
            return Car()

class Car(object):
    def move(self):
        print("move...")

bmw =  CarStore()
res = bmw.order(100000)
res.move