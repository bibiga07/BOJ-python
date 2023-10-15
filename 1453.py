N = int(input())
b = list(map(int,input().split()))
c = 0
a = [0]*100
for i in b:
    if a[i-1] == 0:
        a[i-1] += 1
    else:
        c+=1
print(c)
