import sys
# path = __file__.split('/')
# filename = path.pop()
# path.append(filename.split('-').pop(0) + '.input')
# f = open('/'.join(path), 'r')
M, N = map(int, sys.stdin.readline().strip().split())

def chessMap(origin, num):
  W_ROW = 'WBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWB'
  B_ROW = 'BWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBW'
  line = num
  chess_map = [[0]*N for i in range(M)]
  mask = None
  for i in range(0, M):
    if(num % 2 == 1):
      mask = W_ROW
    else:
      mask = B_ROW
    num += 1
    for j in range(0, N):
      if(origin[i][j] != mask[j]):
        chess_map[i][j] = 1

  return chess_map

  
def solution():
  origin = []
  for i in range(0, M):
    origin.append(list(sys.stdin.readline().strip()))
  WC = chessMap(origin, 1)
  BC = chessMap(origin, 2)
  W_MIN = B_MIN = 2500

  x = y = 0
  for x in range(0, M - 7):
    for y in range(0, N - 7):    
      k = wMin = bMin = 0
      for i in range(x, x + 8):
        for j in range(y, y + 8):
          wMin += WC[i][j]
          bMin += BC[i][j]
      W_MIN = min(wMin, W_MIN)
      B_MIN = min(bMin, B_MIN)

  return min(W_MIN, B_MIN)

print(solution())

