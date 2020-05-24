class Item():
    def __init__(self, itemNumber,itemName, itemWeight,itemPrice,itemRestricted):
        self.itemNumber=itemNumber
        self.itemName=itemName
        self.itemWeight=itemWeight
        self.itemPrice=itemPrice
        self.itemRestricted=itemRestricted

    def getitemNumber(self):
        return self.itemNumber
    
    def getitemName(self):
        return self.itemName

    def getitemWeight(self):
        return self.itemWeight

    def getitemPrice(self):
        return self.itemPrice
    
    def getitemRestricted(self):
        return self.itemRestricted

    def setitemNumber(self, newitemNumber):
        self.itemNumber=newitemNumber

    def setitemName(self, newitemName):
        self.itemName=newitemName

    def setitemWeight(self, newitemWeight):
        self.itemWeight=newitemWeight

    def setitemPrice(self, newitemPrice):
        self.itemPrice=newitemPrice

    def setitemRestricted(self, newitemRestricted):
        self.itemRestricted=newitemRestricted

    def __str__(self):
        return self.itemNumber + ':' + self.itemName + ';' + self.itemPrice