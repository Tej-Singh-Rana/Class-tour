#!/usr/bin/env python
# coding: utf-8

# <<<<<<<<oops method>>>>>>>>>>>>>>>>>>>>>>>>>>>

class computer():
    
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("This is configuration",self.cpu,self.ram)
        
com1=computer("2CPUs","2Gib")
com2=computer("4CPUs","10Gib")
com1.config()
com2.config()


class person:
    def __init__(self):
        self.name="Rock"
        self.age=20
    def update(self):
        self.age=55
        self.name="Undertaker"
    def upgrade(self):
        self.name="Edge"
        self.age=50
x=person()
y=person()

# x.name="stone"
# x.age=45
# y.age=55
x.update()
y.upgrade()
print(x.name,x.age)      
print(y.name,y.age)



class person:
    def __init__(self):
        self.name="Rock"
        self.age=20
        
    def compare(self,other):  #comapre(who is calling(x), whom to compare(y))
        if self.age == other.age:
            return True
        else:
            return False
        
x=person()
y=person()
y.age=40
if x.compare(y):    #compare(who is calling(x)<<x played self role>>,whom to compare(y)<<y played other role>>)
    print("They are same")
else:
    print("They are different")
print(x.name,x.age)      
print(y.name,y.age)

