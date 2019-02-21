import sys
read = sys.stdin.readline

N = int(read())
L = []
SUM = 0
for _ in range(N):
  n = int(read())
  if(n == 0):
    L.pop()
  else:
    L.append(n)

for k in L:
  SUM += k

print(SUM)
(()