import math
import sys
# f = open(__file__[:-2] + 'input', "r")

MAX = 123456 * 2
MAX_SQRT = round(math.sqrt(MAX));
prime = [i for i in range(0, MAX + 2)]
prime[1] = False
for i in range(2, MAX_SQRT):
  if(prime[i] is False):
    continue
  for k in range(2, MAX // 2):
    if i*k <= MAX:
      prime[i*k] = False

def solution():
  while(True):
    n = int(sys.stdin.readline().strip())
    if n == 0:
      break
    n2 = n*2
    sum = 0
    for i in range(n + 1, n2 + 1):
      if(not prime[i] is False):
        sum += 1
    print(sum)
solution()