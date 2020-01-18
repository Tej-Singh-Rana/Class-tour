#!/bin/python3

x = 4
y = 5
z = 7
msg = int(input("Enter your choice : "))

if  msg == x:
    print(" Congratulations You Won!!")

elif msg == y:
    print("Better luck next time!! _/\_ ")

elif msg == z:
    print("Better luck next time!! _/\_ ")

elif  0 <= msg <= 10:
    print("Try again letter -->> ")
    print("######        ########")
    print("######        ########")

elif msg >= 10:
    print("Enter your value below 10")

else:
    print("Enter correct value ")


