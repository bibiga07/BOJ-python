from sys import stdin

for i in range(3):
    a = int(stdin.readline())
    z = 0
    for j in range(a):
        b = int(stdin.readline())
        z += b
    if z == 0:
        print(0)
    elif z < 0:
        print("-")
    elif z > 0:
        print("+")