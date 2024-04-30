class Name:
    def __init__(self, name, age, education) -> None:
        self.name = name
        self.age = age
        self.education= education
        
    def details(self):
        print("My name is", self.name, "and age is", self.age)

    def studies(self):
        print("I am from", self.education)

detailsVarma = Name("Varma", 24, "B.Tech(C.S.E)")
detailsKrishna = Name("Krishna" , 24, "B.Tech(E.C.E)")

detailsVarma.details()
detailsVarma.studies()
detailsKrishna.details()
detailsKrishna.studies()