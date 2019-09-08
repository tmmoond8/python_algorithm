import sys

def scoreCalc(dices):
    s = set([])
    sum = 0
    for i in range(0, 3):
        for j in range(i + 1, 4):
            if dices[i] == dices[j]:
                s.add(dices[i])
                sum += 1

    if sum == 6:
        return 50000 + 5000 * s.pop()
    elif sum == 3:
        return 10000 + 1000 * s.pop()
    elif sum == 2:
        return 2000 + 500 * s.pop() + 500 * s.pop()
    elif sum == 1:
        return 1000 + 100 * s.pop()
    return max(dices) * 100

N = int(sys.stdin.readline().strip())
maxValue = -1
for i in range(0, N):
    line = list(map(int, sys.stdin.readline().strip().split(' ')))
    maxValue = max(maxValue, scoreCalc(line))

print(maxValue)