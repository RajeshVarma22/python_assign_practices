string = "abcdefghijklmnopqrstuvwxyz"
max_width = 4
ls = []
count = 0
subStr = ""
targetCount = 0
times = 0
target = len(string) % max_width
formula = max_width * (len(string) // max_width)


for i in string:
    if (formula == targetCount):
        max_width = target
    if (count <= max_width):
        subStr += i
        count += 1
    if (count == max_width):
        ls.append(subStr)
        subStr = ""
        count = 0
        times += 1
    targetCount += 1
for j in ls:
    print(j)