import sys
# x, y, w, h = map(int, '43 160 124 202'.split(' '))
x, y, w, h = map(int, sys.stdin.readline().strip().split(' '))
def solution():
  minValue = min(x, y, abs(w - x), abs(h - y))
  # done = set()
  # if(x == w or x == 0 or y == 0 or y == h):
  #   return 0
  # q = []
  # q.append((x + 1, y, 1))
  # q.append((x, y +1, 1))
  # q.append((x - 1, y, 1))
  # q.append((x, y -1, 1))

  # done.add((x + 1, y))
  # done.add((x, y + 1))
  # done.add((x - 1, y))
  # done.add((x, y -1))
  # while(q):
  #   _x, _y, _count = q.pop()
  #   # print(_x, _y)
  #   if(_count >= minValue):
  #     continue
  #   if(_x == w or _x == 0 or _y == 0 or _y == h):
  #     minValue = min(_count, minValue)
  #     continue
  #   if(_x < 0 or _y < 0 or _x > w or _y > h ):
  #     continue
  #   if((_x + 1, _y) not in done):
  #     q.append((_x + 1, _y, _count + 1))
  #     done.add((_x + 1, _y))
  #   if((_x, _y +1) not in done):
  #     q.append((_x, _y +1, _count + 1))
  #     done.add((_x, _y +1))
  #   if((_x - 1, _y) not in done):
  #     q.append((_x - 1, _y, _count + 1))
  #     done.add((_x - 1, _y))
  #   if((_x, _y -1) not in done):
  #     q.append((_x, _y -1, _count + 1))
  #     done.add((_x, _y -1))

  return minValue


print(solution())