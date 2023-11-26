a = int(input())
OX = list(map(int, input().split()))
score = 0
b = 1
if OX[0] == 1:
    score += 1
for i in range(1,a):
    if OX[i] == 1:
        score += 1
        if OX[i-1] == 1:
            score += b
            b += 1
    else:
        b = 1
print(score)