def solution(n, lost, reserve):
  count = 0
  for i in lost:
    prevV = i - 1
    nextV = i + 1
    if(i in reserve):
      count += 1
      reserve.remove(i)
    elif(prevV != 0 and prevV in reserve):
      count += 1
      reserve.remove(prevV)
    elif(nextV < n and nextV in reserve):
      count += 1
      reserve.remove(nextV)

  return n - (len(lost) - count)

  # for i in reserve:
  #   prevV = i - 1
  #   nextV = i + 1
  #   if(prevV != 0 and prevV in lost):
  #     lost.remove(prevV)
  #   elif(nextV < n and nextV in lost):
  #     lost.remove(nextV)
  # return n - len(lost)

  

  # T = [1] * n
  # for i in lost:
  #   T[i - 1] = 0
  # for i in reserve:
  #   T[i - 1] = 2
  # for i in range(len(T)):
  #   if i == 0 and n > 1:
  #     if(T[0] == 2 and T[1] == 0):
  #       T[0] = T[1] = 1
  #   else:
  #     if T[i] == 2:
  #       if T[i-1] == 0:
  #         T[i -1] = T[i] = 1
  #       elif i+1 < n and T[i+1] == 0:
  #         T[i + 1] = T[i] = 1
  # sum = 0
  # for i in T:
  #   if i != 0:
  #     sum += 1
  # return sum


print(solution(5, [2, 4], [1, 3, 5]) == 5)
print(solution(5, [2, 4], [3]) == 4)
print(solution(3, [3], [1]) == 2)
