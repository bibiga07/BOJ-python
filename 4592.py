while True:
    C = []
    N = input().split()
    if N[0] == '0':
        break
    N.remove(N[0])
    for i in N:
        if len(C) == 0:
            C.append(i)
        elif C[-1] != i:
            C.append(i)
    C.append('$')
    print(' '.join(C))