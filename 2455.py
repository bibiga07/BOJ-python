firstOUT, firstIN = map(int, input().split())
total = []
total.append(firstIN)
for i in range(2):
    OUT,IN = map(int, input().split())
    firstIN += IN
    firstIN -= OUT
    total.append(firstIN)
secondOUT, secondIN = map(int, input().split())
total.append(firstIN)
print(max(total))
    