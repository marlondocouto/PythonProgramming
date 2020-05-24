class Person():
    def __init__(self, lastname,firstname,phonenumber,email):
        self.lastname=lastname
        self.firstname=firstname
        self.phonenumber=phonenumber
        self.email=email

    def getLastname(self):
        return self.lastname

    def getFirstname(self):
        return self.firstname

    def getPhonenumber(self):
        return self.phonenumber

    def getEmail(self):
        return self.email

    def setLastname(self, newlastname):
        self.lastname = newlastname

    def setFirstname(self, newfirstname):
        self.firstname=newfirstname

    def setPhonenumber(self, newphonenumber):
        self.phonenumber=newphonenumber

    def setEmail (self, newemail):
        self.email = newemail 

    def __str__(self):
        return "This customer is "+self.firstname + " "+ self.lastname+"."

