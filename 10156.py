K, N, M = map(int, input().split())
mom_money = K * N - M
if mom_money <= 0:
    print(0)
else:
    print(mom_money)