import sys
def solution(n):
  n = n.replace('6', '9')
  D = [0 for i in range(0, 10)]
  kkk = list(map(int, list(n)))
  for i in kkk:
    D[i] += 1

  maxValue = 0
  for i in range(0, 9):
    maxValue = max(maxValue,  2 *D[i])
  maxValue = max(maxValue, D[9])
  return maxValue // 2 + maxValue % 2

print(solution(sys.stdin.readline().strip()))
# print(solution('21596068213606568'.replace('6', '9')))