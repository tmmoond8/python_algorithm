import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

if A + B + C != 180:
    print('Error')
elif A == B and B == C:
    print('Equilateral')
elif A == C or B == C or A == B:
    print('Isosceles')
else:
    print('Scalene')
