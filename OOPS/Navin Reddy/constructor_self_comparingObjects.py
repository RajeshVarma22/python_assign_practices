class Person:
    def __init__(self) -> None: # init is a constructer and this constructor is responsible for maintaining the size of the object.
        self.name = "Rajesh" # And size of the class depends upon the number variables you're passing. 
        self.age = 24
    
    def nextYearAge(self):
        self.age = self.age+1

    def compareAge(self, other):
        if self.age == other.age:
            return True
        else:
            return False

p1 = Person()
p2 = Person()
p3 = Person()

print(p1.name)

print(p2.name)
print(p2.age)

p2.name = "Varma"
p2.nextYearAge()

print(p2.name)
print(p2.age)

# For Comparing two obj

print(p1 == p3) # False beacuse both are having different address

print(p1.age, p3.age)

print(p1.compareAge(p3)) # custom method for comparision
