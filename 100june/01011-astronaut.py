import sys
def solution(data):
  start, end = map(int, data.split(' '))
  distance = end - start
  i = 1
  step = 0
  while(True):
    step += i
    if(distance <= step):
      print((i - 1) * 2 + 1)
      return
    step += i
    if(distance <= step):
      print(i *2)
      return
    i += 1

N = int(sys.stdin.readline().strip())
for i in range(0, N):
  solution(sys.stdin.readline().strip())