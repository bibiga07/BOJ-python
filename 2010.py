import sys
input = sys.stdin.readline
N = int(input())
a = 0
for i in range(N):
    a += int(input())
print(a -(N-1))