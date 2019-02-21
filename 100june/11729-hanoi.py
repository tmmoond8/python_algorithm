import sys
D = {
  0: 0,
  1: 1,
  2: 3
}
def hanoi(n):
  if(n not in D):
    D[n] = hanoi(n-1) * 2 + 1
  return D[n]

def movePrint(n, start, mid, end):
  if(n != 1):
    movePrint(n - 1, start, end, mid)
  print('{0} {1}'.format(start, end))
  if(n != 1):
    movePrint(n - 1, mid, start, end)

def solution(n):
  hanoiValue = hanoi(n)
  print(hanoiValue)
  movePrint(n, 1, 2, 3)

solution(int(sys.stdin.readline().strip()))