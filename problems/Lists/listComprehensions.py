x = int(input()) + 1
y = int(input()) + 1
z = int(input()) + 1
n = int(input())
op = []
for i in range(x):
    for j in range(y):
        for k in range(z):
            if (i + j + k != n):
                op.append([i, j, k])
for ans in op:
    print(ans)