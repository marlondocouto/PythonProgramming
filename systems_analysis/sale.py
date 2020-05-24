from item import Item
from orderitem import OrderItem
from payment import Payment
import datetime
import random

class Sale():
    def __init__(self, saleID,saleDate):
        self.salelist=[]
        self.saleID=random.randint(1,100000)
        self.saleDate=datetime.date.today()

    def getsaleID(self):
        return self.saleID

    def getsaleDate(self):
        return self.saleDate

    def addOrderItems(self, orderitem):
        self.salelist.append(orderitem)
    
    def calculateTotal(self):
        total=0.0
        for i in self.salelist:
            total += i.getItem().itemPrice * i.quantity
        payment=Payment(total)
        return payment

    def calculateRewards(self):
        rewards = calculateTotal()/10
        return rewards