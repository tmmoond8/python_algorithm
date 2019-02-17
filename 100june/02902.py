import sys
def solution(str):
  C = []
  c = None
  for i in range(0, len(str)):
    if(c == None and str[i] != '-'):
      c = str[i]
      C.append(c)
    elif (str[i] == '-'):
      c = None
  return ''.join(C)


print(solution(sys.stdin.readline().strip()))