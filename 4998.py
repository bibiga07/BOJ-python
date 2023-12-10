while True:
    try:
        N, B, M = map(float, input().split())
        year = 0
        if N > M:
            break
        while M > N:
            N += N * (B/100)
            year += 1
        print(year)
    except:
        break