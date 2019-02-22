import sys
read = sys.stdin.readline
N = int(read())
L = []
for i in range(N):
  start, end = map(int, read().split(' '))
  L.append((start, end, end - start))

L.sort(key = lambda element : element[2])

start, end, t = L[0]
q = []
q.append((1, 0, set()))
q.append((1, 1, set([i for i in range(start, end)])))
MAX = 0
while q:
  idx, counter, mask = q.pop()
  if idx == N:
    MAX = max(MAX, counter)
    break
  if(N - idx + counter <= MAX):
    continue
  q.append((idx + 1, counter, mask))
  start, end, t = L[idx]
  b = True
  next_mask = set(mask)
  for i in range(start, end):
    if(i in mask):
      b = False
      break
    next_mask.add(i)
  if b:
    q.append((idx + 1, counter + 1, next_mask))

print(MAX)