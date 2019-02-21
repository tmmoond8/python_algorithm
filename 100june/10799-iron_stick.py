import sys
read = sys.stdin.readline

OPEN, CLOSE = '(', ')'
data = read().strip()
SUM = 0
stack = 0
prev = ''

for s in data:
  if s == CLOSE:
    stack -= 1
    if  prev == OPEN:
      SUM += stack
    else:
      SUM += 1
  else:
    stack += 1
  prev = s
  
print(SUM)