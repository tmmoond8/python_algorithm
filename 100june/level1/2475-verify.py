import sys, math

a, b, c, d, e = map(int, sys.stdin.readline().strip().split(' '))

squareSum = math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2) + math.pow(d, 2) + math.pow(e, 2)

print(int(squareSum % 10))