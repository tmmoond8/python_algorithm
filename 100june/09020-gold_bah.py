import math, sys
read = sys.stdin.readline

N = int(read())
MAX = 0
L = []
for _ in range(N):
  k = int(read())
  MAX = max(MAX, k)
  L.append(k)

n = MAX
PRIME = [True]*n
PRIME[0], PRIME[1] = False, False
for i in range(2, math.ceil(math.sqrt(n)) + 1):
  if(PRIME[i]):
    for j in range(2, n):
      if(j*i >= n):
        break
      PRIME[j*i] = False

for k in L:
  half = k // 2
  for s in range(half, k):
    if PRIME[s] and PRIME[k - s]:
      print(str(min(s, k - s)) + ' ' + str(max(s, k - s)) )
      break