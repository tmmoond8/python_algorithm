import sys, math

A, B = map(int, sys.stdin.readline().strip().split(' '))


def sum(a, b):
    return math.floor((a + b) * (b - a + 1) / 2)

print(sum(min(A, B), max(A, B)))