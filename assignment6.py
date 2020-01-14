#assignment6.py
#Program builds acronyms according to what was inputted by user

def main():
    #introduction:
    print("This program creates acronyms according to what is inputted.\n")
    #requesting input from user:
    phrase=input("Please enter the phrase: ")

    #split the phrase into a list:
    list1=phrase.split()

    #create a blank acronym variable:
    acronym=""

    """go through each content of the list,
    grab the 0 index of that content,
    capitalize it, then add it to the previous one until list ends:"""
    for word in list1:
        acronym=acronym+word[0].upper()

    #display output to the user:
    print("Your acronym is: ",acronym)

main()
        
        

    
