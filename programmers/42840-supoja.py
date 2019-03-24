def circleGet(list, length, index):
  return list[index % length]

def solution(answers):
  spj1, l1, c1 = [1, 2, 3, 4, 5], 5, 0
  spj2, l2, c2 = [2, 1, 2, 3, 2, 4, 2, 5], 8, 0
  spj3, l3, c3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 10, 0
    
  for i in range(len(answers)):
    if answers[i] == circleGet(spj1, l1, i):
      c1 += 1
    if answers[i] == circleGet(spj2, l2, i):
      c2 += 1
    if answers[i] == circleGet(spj3, l3, i):
      c3 += 1

  MAX = max(c1, c2, c3)
  answer = []
  if c1 == MAX:
    answer.append(1)
  if c2 == MAX:
    answer.append(2)
  if c3 == MAX:
    answer.append(3)
  return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))