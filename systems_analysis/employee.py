from person import Person

class Employee(Person):
    def __init__(self, lastname,firstname,phonenumber,email,employeeID,accesslevel):
        super().__init__(lastname,firstname,phonenumber,email)
        self.employeeID=employeeID
        self.accesslevel=accesslevel

    def getemployeeID(self):
        return self.employeeID

    def getaccesslevel(self):
        return self.accesslevel

    def __str__(self):
        message="Your employee ID is " +str(self.employeeID)+"."
        return message

    
