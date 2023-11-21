z = []
for i in range(10):
    a = int(input())
    b = a%42
    z.append(b)

x = []
for i in z:
    if i not in x:
        x.append(i)
print(len(x))