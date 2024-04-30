class Factors:
    def __init__(self, num) -> None:
        self.num = num
    
    def main(self):
        factors = []
        for i in range(1, self.num+1):
            if(self.num % i == 0):
                factors.append(i)

        for j in factors:
            print(j)
    

inp = int(input("Enter a number:"))
myNum = Factors(inp)
myNum.main()