import sys
def console(block):
  for a in block:
    print(''.join(a))

def process(left, top, n, block):
  third = n//3
  for i in range(0, 9):
    x, y  = i % 3, i // 3
    if(third == 1):
      if(i != 4):
        block[top + y][left + x] = '*'
    else:
      if(i != 4):
        process(left + third*x, top + third*y, third, block)
def solution(n):
  if(n == 1):
    print('*')
    return
  block = [[' ']*n for i in range(n)]
  process(0, 0, n, block)
  console(block)

# solution(3)
# solution(9)
solution(int(sys.stdin.readline().strip()))