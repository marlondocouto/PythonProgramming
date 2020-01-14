def phrase():
    #prompt user to enter the input(sentence):
    print("The program calculates number of words in a sentence")
    print()
    phrase=input("Please, enter a phrase: ")
    #using split to generate the list of words from sentence entered:
    List=phrase.split()
    print()
    #generating the output:
    print("The number of words is: ",str(len(List))+".")
    print()

    x=input("Press <ENTER> to quit program")    
    

phrase()
