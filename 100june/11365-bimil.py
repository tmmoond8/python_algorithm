import sys
def process(str):
  reversed = ''
  length = len(str)
  for i in range(0, length):
    reversed += str[length - 1 - i]
  return reversed

def solution():
  # path = __file__.split('/')
  # filename = path.pop()
  # path.append(filename.split('-').pop(0) + '.input')
  
  # f = open('/'.join(path), 'r')
  while(True):
    line = sys.stdin.readline().strip()
    if(line == 'END'):
      break
    print(process(line))

solution()
# print('sdfsdfdsff\tdsfdfdsf\n')
