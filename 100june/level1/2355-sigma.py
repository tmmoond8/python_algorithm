import sys

low, high = map(int, sys.stdin.readline().strip().split(' '))
# low, high = 1, 2

sum = 0

while True:
    sum += low + high
    low = low + 1
    high = high - 1
    if low == high or high < low:
        break
print(sum)

#PASS