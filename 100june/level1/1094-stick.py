import sys
N = int(sys.stdin.readline().strip())

sticks = [64]

while sum(sticks) > N:
    min = sticks.pop()
    if (sum(sticks) + min/2) >= N:
        sticks += [min/2]
    else:
        sticks += [min/2, min/2]

print(len(sticks))