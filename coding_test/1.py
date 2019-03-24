import math
MAX = 1000
MAX_SQRT = int(round(math.sqrt(MAX)))
prime = [True]* (MAX + 2)
prime[1] = False
for i in range(2, MAX_SQRT):
  if(prime[i] is False):
    continue
  for k in range(2, MAX // 2):
    if i*k <= MAX:
      prime[i*k] = False


q = []
def solution(n):
  SUM = 0
  q.append((n, 3, []))
  while q:
    number, count, history = q.pop()
    if len(history) == 0:
      i = 2
    else:
      i = history[len(history)-1] + 1
    if count == 0:
      if number == 0:
        SUM += 1
    while i <= number:
      if prime[i] != False and number - i >= count - 1:
        q.append((number - i, count - 1, history + [i]))
      i += 1
  return SUM

print(solution(33))


