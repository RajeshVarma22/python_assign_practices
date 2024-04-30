# num = 8

# if num % 2 == 0:
#     res = 1
#     for i in range(2):
#         res *= num
#     print(res)
# else:
#     resCube = 1
#     for i in range(3):
#         resCube *= num
#     print(resCube)
    
    
stratHrs, startMins = map(int,"12:30".split(":"))
endHrs, endMins = map(int, "13:30".split(":"))

game_timigs = [00, 15, 30, 45]

cycles = 0

if(startMins in game_timigs):
    hrs_mins = (endHrs - stratHrs) * 60
    remaining_mins = (endMins - startMins)
    total_mins = hrs_mins + remaining_mins
    cycles = total_mins // 15
else:
    hrs_mins = (endHrs - stratHrs) * 60
    startTime = 0
    for j in game_timigs:
        if(j > startMins):
            startTime = j
            break
    total_mins = (endMins - startTime) + hrs_mins
    cycles = (total_mins // 15)

print(cycles)
