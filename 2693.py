a = int(input())
for i in range(a):
    b = list(map(int,input().split()))
    b.sort()
    print(b[-3])