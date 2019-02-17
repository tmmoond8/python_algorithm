import sys
dest = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip())

# path = __file__.split('/')
# filename = path.pop()
# path.append(filename.split('-').pop(0) + '.input')
# f = open('/'.join(path), 'r')
# dest = f.readline().strip()
# N = int(f.readline().strip())
HAVE = [True for i in range(10)]
exclude = []
if(N > 0):
  exclued = list(map(int, sys.stdin.readline().strip().split()))
  for i in exclued:
    HAVE[i] = False

destValue = int(dest)

def solution():
  d = ['*' for i in range(len(dest))]
  q = []
  q.append(''.join(d))
  if(len(dest) > 1):
    q.append('0' + q[0][1:])
  minValue = 500000
  while(q):
    item = q.pop(0)
    xIndex = item.find('*')
    if(xIndex == -1):
      minValue =  min(
        abs(int(item) - destValue) + len(str(int(item))),
        minValue
      )
      continue
    q_b = []
    for i in range(0, 10):
      candidate = item[0:xIndex] + str(9 - i) + item[xIndex + 1:]
      if(HAVE[9 - i] and candidate <= dest):
        q_b.append(candidate)
    q = q_b + q
  
  d = ['x' for i in range(len(dest))]
  q.append(''.join(d))
  q.append('x' + q[0])
  maxValue = 500000
  while(q):
    item = q.pop(0)
    xIndex = item.find('x')
    if(xIndex == -1):
      maxValue = min(
        abs(int(item) - destValue) + len(dest),
        maxValue
      )
      continue
    q_b = []
    for i in range(0, 10):
      candidate = item[0:xIndex] + str(i) + item[xIndex + 1:]
      if(HAVE[i] and int(candidate.replace('x', '9')) >= destValue):
        q_b.append(candidate)
    q = q_b + q
  
  return min(
    minValue,
    maxValue,
    abs(100 - destValue)
  )

print(solution())