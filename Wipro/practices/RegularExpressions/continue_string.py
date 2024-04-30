# import re

# pattern = '^a...s$'
# string = "This is agels"
# res = re.match(pattern, string)

# print(res)

# st = "Hello"
# st1 = st

# print(id(st))
# print(id(st1))

# st += "Raj"

# print(id(st))
# print(id(st1))

n = int(input())
# ans = []


for i in range(n):
    lenS = int(input())
    string = input()
    mSum = 0
    
    for i in range(lenS - 3): 
        firstPair = int(string[i:i+2])  
        
        for j in range(i+2, lenS-1): 
            secondPair = int(string[j:j+2])  
            preSum = firstPair + secondPair
            if preSum > mSum and preSum != 11: 
                mSum = preSum
    print(mSum)