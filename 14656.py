N = int(input())
people = list(map(int, input().split()))
people_sort = people.copy()
people_sort.sort()
bbadda = 0
for i in range(N):
    if people_sort[i] != people[i]:
        bbadda += 1
print(bbadda)
    