n = int(input())
changyeong = 100
sangdeok = 100
for i in range(n):
    c,s = map(int, input().split())
    if c > s:
        sangdeok -= c
    elif c < s:
        changyeong -= s
print(changyeong)
print(sangdeok)