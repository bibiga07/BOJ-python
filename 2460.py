toOUT, toIN = map(int,input().split())
totalmax = []
totalmax.append(toIN)
a = toIN
for i in range(1,9):
    OUT, IN = map(int,input().split())
    a -= OUT
    a += IN
    totalmax.append(a)
toOUT, toIN = map(int,input().split())
a -= toOUT
totalmax.append(a)
print(max(totalmax))


