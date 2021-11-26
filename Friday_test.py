for item in range(1,11):
    print(item)

while item in range(10):
    print(item)

print(range(10))

item = 20

while item == 20:
    print(item)
    item +=1

while False:
    print(1)

class Lvl1(object):
    hello = "hello"
    def __init__(self,var):
        self.var = var
        self._d = 100

    def return_var(self):
        self.var +=1
        return self.var

class Lvl2(Lvl1):
    def __init__(self,var,var1=2):
        Lvl1.__init__(self,var)
        self.var1 = var1

#printtype(Lvl1.var)
item1 = Lvl2(30,22)
print(item1.var)
print(item1.return_var())
print(item1.hello)
print(Lvl1.hello)
print(item1.var1)
print(item1._d)

