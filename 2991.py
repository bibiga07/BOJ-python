A,B,C,D = map(int,input().split())
z = list(map(int,input().split()))
for i in z:
    attack = 0
    if 0 < i%(A+B) <= A:
        attack += 1
    if 0 < i%(C+D) <= C:
        attack += 1
    print(attack)
