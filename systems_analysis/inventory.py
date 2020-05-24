from item import Item

class Inventory():
    def __init__(self):
        self.items=[]

    def addItem(self,item):
        self.items.append(item)

    def getItems(self):
        return self.items

    def getItemNumber(self, number):
        reqItem=None
        for i in self.items:
            if i.itemNumber==number:
                reqItem=i
                break
        return reqItem