from heapq import *
import bisect

def solution(healths, items):
  healths.sort()
  for i in range(len(items)):
    items[i].append(i + 1)
  items.sort()

  answer = []
  while items:
    attack, need_health, index = map(int, items.pop())
    idx = bisect.bisect_left(healths, need_health + 100)
    if idx == len(healths):
      continue
    del healths[idx]
    heappush(answer, index)
  return answer


print(solution([500, 240], [[530, 200], [100, 30]]) == [1, 2])