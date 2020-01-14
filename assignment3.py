#assignment3.py
#Calculates the cost per square inch of a circular pizza

import math #makes math library available
def cost_square():
    #introduction to program
    print("This program computes the cost per square inch of a pizza.")
    print()
    #inputs are diameter and price of pizza:
    diameter=int(input("Enter the diameter of the pizza (in inches): "))
    price=int(input("Enter the price of the pizza (in cents): "))
    #processing of input:
    cost_square=price/(((diameter/2)**2)*math.pi)
    print()
    #output message:
    print("The cost per square inch is", round(cost_square,2))
    print()
    input("Press the <Enter> key to shut down the program")
    

cost_square()
