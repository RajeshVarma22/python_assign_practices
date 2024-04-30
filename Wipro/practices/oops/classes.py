class Name:
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def printDetails(self):
        print("Hi my name is {} and my age is {}.".format(self.name, self.age))

rajesh = Name("Rajesh Varma", 24)
rajesh.printDetails()