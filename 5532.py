L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A%C > 0:
    X = A//C+1
else:
    X = A//C
if B%D > 0:
    Y = B//D+1
else:
    Y = B//D
Z = []
Z.append(X)
Z.append(Y)
print(L-max(Z))