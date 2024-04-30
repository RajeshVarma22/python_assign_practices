class A:
    a = 1
    b = 2
    
    def getAB(cl):
        print("Working")
        print(cl.a, cl.b)

n = A()
n.getAB()

class B(A):
    a = 1.1
    b = 2.2
    

n1 = B()
n1.getAB()