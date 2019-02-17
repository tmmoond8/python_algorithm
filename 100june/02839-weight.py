def solution(weight):
  n5 = weight // 5
  n3 = (weight % 5) // 3
  
  return 1



print(solution(18) == 4)
print(solution(4) == -1)
print(solution(6) == 2)
print(solution(9) == 3)
print(solution(11) == 3)