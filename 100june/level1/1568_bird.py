import sys

N = int(sys.stdin.readline())
n, i, counter = N, 1, 0

while(True):
    if i == n:
        counter += 1
        print(counter)
        break
    if i > n:
        i = 1
        continue
    n -= i
    i += 1
    counter += 1
