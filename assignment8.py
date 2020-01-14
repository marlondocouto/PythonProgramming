#assingment8.py
#Author: Marlon Do Couto
#A program that calculates payment according to hours worked in a week

def main():
    print("This program calculates your weekly total pay.\n")

    #input from user - wage and hours worked
    wage=float(input("What is your hourly wage? "))
    hours=float(input("How many hours did you work this week? "))

    """processing through if statements
    if user worked more than 40 hours then total wage will be
    a combination of the first 40 hours * wage
    plus the additional hours *1.5*wage:"""
    
    if hours>40:
        total_wage1=40*wage
        total_wage2=(hours-40)*1.5*wage
        #output:
        print("\nYour total weekly pay is ",total_wage1+total_wage2)
    #if user did not work over 40 hours, then calculation is straigh forward:
    else:
        total_wage=wage*hours
        #output:
        print("\nYour total weekly pay is ",total_wage)

main()
