#!/usr/bin/env python
# coding: utf-8

# <<<<<<<<<<<<------------------ _init_method--------------------->>>>>>>>>>>>>>>>>>>


class computer():
    
    def __init__(self):   #It will print automatically itself. How many times object call it will print the same count.
        print("Hello folks")
        
    def core(self):
        print("16Gib, 4vCPU, 12TB")
            
com1=computer()    #__init__ method follows objects.
com2=computer()
com1.core()
computer.core(com1)
com2.core()


import time
class car():
    
    def __init__(self,car,color):  #each objects has their own values so it will call itself own values.
        self.car = car
        self.color = color
        
    def gen(self):                      #we are defining in this method to add extra features.
        print("Details about car ", self.car)
        time.sleep(1)
        print("color of car ",self.car,"is",self.color)
            
car1=car("audi","red")
car2=car("ferari","black")
car3=car("bmw","white")
print("Details of car :- ")
time.sleep(2)
car1.gen()
time.sleep(2)
car2.gen()
time.sleep(2)
car3.gen()
time.sleep(2)
car.gen(car2)



class video():
    
    def __init__(self,best,worst):
        self.best = best
        self.worst = worst
    
    def movie(self):
        print("Movie ratings :- ")
        x = int(input())
        if x <= 5:
            print("Below rating 5 not good at all",self.worst)
        elif x > 5:
            print("Greater then rating 5 is quite good",self.best)

movie1=video("Baaghi3","Jumanji")
movie2=video("Bloodshot","Widow Women" )

movie1.movie()
movie2.movie()   
