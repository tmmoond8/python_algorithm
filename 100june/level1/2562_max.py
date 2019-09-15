import sys

MAX = 0
idx = -1
for i in range(0, 9):
    n = int(sys.stdin.readline().strip())
    if n > MAX:
        MAX, idx = n, i

print(MAX)
print(idx + 1)