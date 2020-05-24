class Payment():
    def __init__(self, paymentamount):
        self.paymentamount=paymentamount

    def __str__(self):
        self.paymentamount=round(self.paymentamount,2)
        message="Your payment total is "+ str(self.paymentamount)+"."
        return message

