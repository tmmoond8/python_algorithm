import sys
def solution(n):
  counter = 1
  index = 0
  while(True):
    if(str(counter).find('666') != -1):
      index += 1
    if(index == n):
      return counter
    counter += 1


print(solution(int(sys.stdin.readline().strip())))