from heapq import *

def solution(scoville, K):
  heapify(scoville)
  H = scoville
  count = 0

  while True:
    MIN = heappop(H)
    if MIN >= K:
      return count
    if len(H) > 0:
      MINN = heappop(H)
      heappush(H, MIN + 2*MINN)
      count += 1
    else:
      return -1
  return count


print(solution([1, 2, 3, 9, 10, 12], 7) == 2)