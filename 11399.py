a = int(input())
z = a
b = list(map(int,input().split()))
c = 0
b.sort()
for i in range(a):
    for j in range(z-1,-1,-1):
        c += b[j]
    z -= 1
print(c)