def fractionLowest(n1, n2):
    lowesFractionU = 1
    lowesFractionD = 1
    for i in range(2, n1+1):
        if(n1 % i == 0 and n2 % i == 0):
            lowesFractionU = n1 // i
            lowesFractionD = n2 // i
            break
    return lowesFractionU, lowesFractionD

inp1, inp2 = int(input()), int(input())

res = fractionLowest(inp1, inp2)
print(res)

