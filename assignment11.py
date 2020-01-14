#Assignment11.py
#Author: Marlon Do Couto (with some webresearch help)
#function returns list in a shuffled manner:

from random import randrange


def shuffle (myList):
    list1 = []
    for i in range(len(myList)):
        itemToMove = randrange(0, len(myList))
        list1.append(myList[itemToMove])
        myList.pop(itemToMove)
    return list1

print(shuffle([1,2,3,4,5,6,7,8,9,10]))
