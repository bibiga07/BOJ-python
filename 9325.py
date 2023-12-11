a = int(input())
for i in range(a):
    s = int(input())
    n = int(input())
    for j in range(n):
        q, p = map(int, input().split())
        s += q*p
    print(s)