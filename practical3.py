#!/bin/python3

#discount,quantity,cost.

print("Enter your total unit : ")
user=float(input())
unit=100
total=unit * user
print("Total amount: ",+ total)
if total <= 1000:
    print(total)
elif total > 1000 :
    discount= total * .10
    print("10% discount applied", + discount)
    amount = total - discount
    print(amount)
