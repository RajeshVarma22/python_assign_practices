# A Anonymous function is callled as lambda function
''' Python lambda is a single line single expression anonymous function it can take mutiple args and only gives single output.'''

lambda x, y : x + y

rangeList = [ i for i in range(5)]
print(rangeList) # [0, 1, 2, 3, 4]

sum = [ j+j for j in range(10)]
print(sum) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

square = [ j**j for j in range(10)]
print(square) # [1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]

even = [ (j % 2 == 0) for j in range(1, 10)]
print(even) # [False, True, False, True, False, True, False, True, False] 

lst = [1,4,3,6,45,56,4,8,9,10,23,56,22]
maximum = max(lst)
print(maximum)