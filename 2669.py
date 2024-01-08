x = [[0 for i in range(100)]for j in range(100)]
for i in range(4):
    a,b,c,d = map(int,input().split())
    for j in range(a,c):
        for k in range(b,d):
            x[j][k] += 1
y = 0
for i in range(100):
    for j in range(100):
        if x[i][j] > 0:
            y+=1
print(y)