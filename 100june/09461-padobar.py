import sys
read = sys.stdin.readline

P = [-1] * 101
P[0], P[1], P[2], P[3], P[4], P[5] = 0, 1, 1, 1, 2, 2

def padoban(n):
  if n < 0 :
    return 0
  if P[n] != -1:
    return P[n]
  P[n] = padoban(n-1) + padoban(n - 5)
  return P[n]

def solution():
  N = int(read())
  for _ in range(N):
    print(padoban(int(read())))

solution()
