from heapq import *

def solution(people, tshirts):
  people_heap, tshirts_heap = [], []

  for p in people:
    heappush(people_heap, (-p, p))
  for t in tshirts:
    heappush(tshirts_heap, (-t, t))

  SUM = 0
  big_t = heappop(tshirts_heap)[1]
  big_p = heappop(people_heap)[1]
  while True:
    if big_t < big_p:
      if len(people_heap) == 0:
        break
      big_p = heappop(people_heap)[1]
    else:
      SUM += 1
      if len(people_heap) == 0 or len(tshirts_heap) == 0:
        break
      big_t = heappop(tshirts_heap)[1]
      big_p = heappop(people_heap)[1]
  
  return SUM

# def solution(people, tshirts):
#   people.sort()
#   tshirts.sort()
#   SUM = 0
#   LEN_T = len(tshirts)

#   for t in tshirts:
#     if t in people:
#       people.remove(t)
#       SUM += 1

#   while tshirts:
#     t = tshirts.pop()
#     if len(people) > 0:
#       p = people.pop()
#     else:
#       break
#     if t >= p:
#       SUM += 1
  
#   return SUM

print(solution([2, 3], [1, 2, 3]) == 2)
print(solution([1, 2, 3], [1, 1]) == 1)