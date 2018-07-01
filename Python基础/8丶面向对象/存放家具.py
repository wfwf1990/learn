# Author: wangfang
class Home:
    def __init__(self,new_area,new_type,new_addr):
        self.area = new_area
        self.type = new_type
        self.addr = new_addr
        self.re_area = new_area
        self.furniture = []
    def __str__(self):
        msg = "你的房子面积是%d平方,户型是%s,地址是在%s!" %(self.area,self.type,self.addr)
        msg += "你的家具是%s" %self.furniture
        msg += "剩余面积%s平方" %self.re_area
        return msg

    def AddFurniture(self,item):
        #self.furniture.append(item.name)
        #self.re_area -= item.area
        self.re_area -= item.GetArea()
        self.furniture.append(item.GetName())
class Bed:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        msg = "床的名字是%s,占地面积是%d平方" %(self.name,self.area)
        return msg
    def GetName(self):
        return self.name
    def GetArea(self):
        return self.area



fangzi1 = Home(132,"3室两厅","北京天安门")
print(fangzi1)

bed1 = Bed("席梦思",4)
print(bed1)
fangzi1.AddFurniture(bed1)
print(fangzi1)