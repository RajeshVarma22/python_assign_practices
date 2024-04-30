array = [44, 33, 88, 22, 77, 66, 68, 52, 10, 5, 11]


for i in range(len(array) - 1): # 4 times repetition
    for j in range(len(array)-(i+1)): # 4 times first
        if(array[j] > array[j+1]):
            swap = array[j]
            array[j] = array[j+1]
            array[j+1] = swap

# print(array)


a2 = [44, 33, 88, 22] 


for i in range( len(a2) - 1 ):
    startIndex = i

    for j in range(i+1, n):

        # if(a2[])
        
    
    # if(maxNum > a2[i]):
    #     a2[i], a2[i+1] = a2[i+1], a2[i]
    # else:
    #     maxNum = a2[i]

print(a2)