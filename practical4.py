#!/bin/python3

#bonus calculator!!
bonus=0.05
print("Enter your salary : ")
salary=float(input())
print("Enter your service period year : ")
service=int(input())
year=5
if service <= year:
    print("not eligible")
elif service > year:
        print("Net Bonus Calculated : ")
        netbonus=salary*bonus
        print("%.2f"%netbonus)
        print("Total amount included bonus : ")
        print("%.2f"%(netbonus+salary))
