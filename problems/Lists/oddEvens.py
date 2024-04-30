n = input().split(" ")
evenNum = ""
oddNum = ""
for i in n:
    if((int(i)) % 2 == 0):
        evenNum += i + " "
    else:
        oddNum += i + " "

print(evenNum+oddNum)