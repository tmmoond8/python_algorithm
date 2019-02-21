import sys
def console(block):
  for a in block:
    print(''.join(a))
    
def solution(left, top, n, block):
  if(n == 3):
    for i in range(0, 3):
      for j in range(0, 5):
        if (i != 1 or j % 2 != 0) and (i != 2 or j == 2):
          block[top -1 - i][left + j] = '*'
  else:
    half = n // 2
    solution(left, top, half, block)
    solution(left + half, top - half, half, block)
    solution(left + half * 2, top, half, block)
  return


n = int(sys.stdin.readline().strip())

block = [[' '] * (n * 2 - 1) for i in range(n)]
solution(0, n, n, block)
console(block)