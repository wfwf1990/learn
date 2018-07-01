# Author: wangfang

class SweetPotato:
    def __init__(self):
        self.type = "生的"
        self.time = 0
        self.burden = []
    def __str__(self):
        msg = "烤了%d分钟,地瓜是%s" %(self.time,self.type)
        msg += "当前的配料是%s" %str(self.burden)
        return msg
    def roast_sweet_potato(self,time):
        self.time += time
        if self.time >= 0 and self.time < 3:
            self.type = "生的"
        elif self.time >= 3 and self.time < 5:
            self.type = "半生不熟"
        elif self.time >= 5 and self.time < 8:
            self.type = "熟了"
        elif self.time >= 8:
            self.type = "烧焦了"
    def AddBurden(self,bur):
        self.burden.append(bur)
res = SweetPotato()
print(res)
res.AddBurden("甜的")
res.AddBurden("辣的")
res.roast_sweet_potato(1)
print(res)
res.roast_sweet_potato(1)
print(res)
res.roast_sweet_potato(1)
print(res)
res.roast_sweet_potato(1)
print(res)
res.roast_sweet_potato(1)
print(res)
res.roast_sweet_potato(1)
print(res)
res.roast_sweet_potato(1)
print(res)
res.roast_sweet_potato(1)
print(res)
res.roast_sweet_potato(1)
print(res)