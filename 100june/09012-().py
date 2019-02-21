import sys
read = sys.stdin.readline

OPEN, CLOSE = '(', ')'
def solution(data):
  openL = 0
  for i in data:
    if i == CLOSE:
      if openL < 1:
        return 'NO'
      else:
        openL -= 1
    else:
      openL += 1
  
  if openL == 0:
    return 'YES'
  else:
    return 'NO'
  return 'YES'

N = int(read())
for _ in range(N):
  print(solution(read().strip()))