# f = open(__file__[:-2] + 'input', "r")
import sys
def solution():
  count = [0*i for i in range(0, 8001)]
  sum = 0
  MIN, MAX = 8000, 0
  frequency = (0, [])
  # N = int(f.readline().strip())
  N = int(sys.stdin.readline().strip())
  for i in range(0, N):
    # n = int(f.readline().strip()) + 4000
    n = int(sys.stdin.readline().strip()) + 4000
    sum += n
    count[n] += 1
    MIN = min(MIN, n)
    MAX = max(MAX, n)
    if(count[n] > frequency[0]):
      frequency = (count[n], [n])
    elif(count[n] == frequency[0]):
      frequency[1].append(n)
    
  freqSum = 0
  mid = N // 2 + 1
  for i in range(0, 8001):
    if(count[i] != 0):
      freqSum += count[i]
      if(freqSum >= mid):
        mid = i - 4000
        break
  
  if len(frequency[1]) == 1:
    freq = frequency[1].pop()
  else:
    minV = min(frequency[1])
    frequency[1].remove(minV)
    freq = min(frequency[1])
  print(round((sum - 4000* N) /N))
  print(mid)
  print(freq - 4000)
  print(MAX - MIN)
solution()