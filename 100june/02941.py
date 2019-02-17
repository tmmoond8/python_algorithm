import sys

def solution(str):
  table = {
    'c': ['=', '-'],
    'd': ['z=', '-'],
    'l': ['j'],
    'n': ['j'],
    's': ['='],
    'z': ['=']
  }
  size = 0
  skip = 0
  for i in range(0, len(str)):
    if(skip > 0):
      skip -= 1
      continue
    if(str[i] in table):
      croMap = table[str[i]]
      for j in croMap:
        if(str.startswith(j, i + 1)):
          skip += len(j)
    size += 1
  return size

print(solution(sys.stdin.readline().strip()))

# print(solution('ljes=njak') == 6)
# print(solution('ddz=z=') == 3)
# print(solution('nljj') == 3)
# print(solution('dz=') == 1)
# print(solution('c=c=') == 2)