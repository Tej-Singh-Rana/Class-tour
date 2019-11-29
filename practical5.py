#!/bin/python3

#grading system!!

print("Enter your marks: ")
x=float(input())
if (x > 0):
    if x < 25:
        print("grade F ")
    elif x <45:
        print("grade E")
    elif x < 50:
        print("grade D")
    elif x < 60:
        print("grade C")
    elif x < 80:
        print("grade B")
    elif x <= 100:
        print("grade A")
    else:
        print("out of range")
else:
    print("Failed")
