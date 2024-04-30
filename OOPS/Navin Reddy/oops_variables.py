# Two types of variables are in ooops. 
# 1) Instance Variable (If you define a variable inside init it is called as Instance Variable)
# 2) ClasS(Static) Variable (If you define a variable above the init function the it's called as Static Variable / Class Variables And nameSpace)


class Bike:
    
    wheels = 2
    
    def __init__(self, cc, color, milage, comp) -> None:
        self.cc = cc
        self.color = color
        self.milage = milage
        self.comp = comp


yamaha
