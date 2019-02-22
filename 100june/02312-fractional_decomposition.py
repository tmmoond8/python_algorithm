import sys
read = sys.stdin.readline

def solution(data):
  fraction = [False ]* (data + 1)
  for i in range(2, data + 1):
    if data == 1:
      break
    while data % i == 0:
      fraction[i] += 1
      data = data / i
  
  for k in range(2, len(fraction)):
    if fraction[k] != False: print(str(k) + ' ' + str(fraction[k]) )
  
N = int(read())
for _ in range(N):
  n = int(read())
  solution(n)

# solution(3)
# solution(3984)
