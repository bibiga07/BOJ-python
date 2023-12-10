T = int(input())
for i in range(1,T+1):
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print("Case %d: %d" %(i,A+B))