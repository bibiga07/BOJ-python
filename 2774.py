T = int(input())
for i in range(T):
    count = []
    X = input()
    for j in X:
        if j not in count:
            count.append(j)
    print(len(count))