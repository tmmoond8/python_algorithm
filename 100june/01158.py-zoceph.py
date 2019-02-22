import sys
read = sys.stdin.readline

N, M = map(int, read().split(' '))
x = 1
L = [i for i in range(1, N + 1)]
E = []
prev = 0

while L:
  length = len(L)
  x = -1 
  count = 0

  LB = []
  while x < length:
    x += 1
    if x >= length:
      continue
    if (x + 1 + prev) % M == 0:
      E.append(str(L[x]))
      count += 1
    else:
      LB.append(L[x])
  L = LB
  prev = length - count*M

print('<' + ', '.join(E) + '>')