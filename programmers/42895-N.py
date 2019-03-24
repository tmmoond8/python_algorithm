import sys
D = {}
MIN = -1
STOP = False
def d(n, k, D, number):
  global MIN, STOP
  if STOP:
    return set([])
  if n in D:
    return D[n]
  if n == 1:
    D[n] = [k]
    return D[n]
  D[n] = set([int(str(k)*n)])
  for i in range(1, n):
    for a in d(i, k, D, number):
      for b in d(n-i, k, D, number):
        D[n].add(a + b)
        D[n].add(a - b)
        D[n].add(a * b)
        if b != 0:
          D[n].add(a // b)
  if(number in D[n] and MIN == -1):
    MIN = n
    STOP = True
  return D[n]

def solution(N, number):
  d(8, N, D, number)
  return MIN

solution(5, 12)