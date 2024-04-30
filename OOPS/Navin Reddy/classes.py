class Animal:
    def __init__(self) -> None:
        self.dog = "Bark"
        self.lion = "Roar"


animal1 = Animal()

print(animal1.dog, animal1.lion)

class MobileSpecs:
    
    def config(self):
        print("RAM :-",6, "ROM :-",128, "CPU :-","SD 888 gen 3")
        
config1 = MobileSpecs()

config1.config()

# MobileSpecs.config(config1) 

