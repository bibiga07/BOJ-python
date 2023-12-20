N, L = input().split()
N = int(N)
cnt = 0
a = 1
while cnt != N:
    if str(L) not in str(a):
        b = a
        cnt += 1
    a+=1
print(b)