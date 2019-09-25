import sys

top = (-1, 0)

for i in range(0, 5):
    scores = sum(list(map(int, sys.stdin.readline().strip().split(' '))))
    if top[1] < scores:
        top = (i + 1, scores)


print(top[0], top[1])