M = int(input())
cup = [1,0,0]
for i in range(M):
    X, Y = map(int, input().split())
    cup[X-1], cup[Y-1] = cup[Y-1], cup[X-1]
    print(cup)

if cup[0] == 1:
    print(1)
elif cup[1] == 1:
    print(2)
elif cup[2] == 1:
    print(3)
else:
    print(-1)

