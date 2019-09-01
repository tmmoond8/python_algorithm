import sys

N = int(sys.stdin.readline())
arr = []

for i in range(1, N):
    arr.append(N * i + i)

print(sum(arr))