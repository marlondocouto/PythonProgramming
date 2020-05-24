from person import Person
import random

class Customer(Person):
    def __init__(self, lastname, firstname, phonenumber,email,customerID,customerCard):
        super().__init__(lastname,firstname,phonenumber,email)
        self.customerID = self.phonenumber
        self.customerCard=customerCard
    
    def getcustomerID(self):
        return self.customerID

    def getcustomerCard(self):
        return self.customerCard

    def setcustomerID (self, newID):
        self.customerID=newID

    def setcustomerCard(self, newcard):
        self.customerCard=newcard

    def __str__(self):
        message = "Your customer ID is " + str(self.customerID)+"."
        return message


