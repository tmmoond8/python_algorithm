def solution(priorities, location):
  MAX = list(priorities)
  MAX.sort(reverse=True)
  i = counter = 0
  while True:
    if priorities[i] < MAX[counter]:
      priorities.append(priorities[i])
      if i == location:
        location = len(priorities) - 1
    else:
      counter += 1
      if location == i:
        return counter
    i += 1


print(solution([2, 1, 3, 2], 2) == 1)
print(solution([1, 1, 9, 1, 1, 1], 0) == 5)