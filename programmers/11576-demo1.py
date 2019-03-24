def solution(v):
  x1 = v[0][0]
  x2 = v[1][0]
  x3 = v[2][0]

  y1 = v[0][1]
  y2 = v[1][1]
  y3 = v[2][1]
  
  if x1 == x2:
    x = x3
  elif x1 == x3:
    x = x2
  else:
    x = x1


  if y1 == y2:
    y = y3
  elif y1 == y3:
    y = y2
  else:
    y = y1

  return [x, y]


print(solution([[1, 4], [3, 4], [3, 10]]))
print(solution([[1, 1], [2, 2], [1, 2]]))