import sys

def yoot(arr):
    sum = 0
    for i in range(0, 4):
        if arr[i] == 1:
            sum += 1
    if sum == 0:
        return 'D'
    elif sum == 1:
        return 'C'
    elif sum == 2:
        return 'B'
    elif sum == 3:
        return 'A'
    else:
        return 'E'


for i in range(0, 3):
    data = list(map(int, sys.stdin.readline().strip().split(' ')))
    print(yoot(data))