a = list(map(int,input().split()))
z = input()

a.sort()

for i in z:
    if i == 'A':
        print(a[0], end=" ")
    elif i == 'B':
        print(a[1], end=" ")
    else:
        print(a[2], end=" ")


