class Person:
    def __init__(self,id):
        self.id = id
        print("Instance of this class is created")

    def __del__(self):
        print(self.id,"Instance of this class is deleted")
        
    def setFullName(self,fName,lName):
        self.fName = fName
        self.lName = lName
        
    def printFullName(self):
        print(self.fName,self.lName)

personName = Person(5)
personName.setFullName("MS","Dhoni")
personName.printFullName()
personName.__del__()

