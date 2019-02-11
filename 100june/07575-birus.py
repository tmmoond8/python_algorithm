# def find_candidate(src, dest, candidate):
#   if(len(src) < 1):

# print(find_candidate("11 22", "11 22 44"))
# print(find_candidate("44 22", "44 21 32"))


def solution():
  f = open(__file__.split('-')[0] + "-input.txt", 'r')
  [N, K] = f.readline().split(" ")
  N, K = int(N), int(K)
  min = {
    'min': {
      'value': 1000,
      'index': -1
    },
    'min2': {
      'value': 1000,
      'index': -1
    }
  }
  input = []
  for i in range(0, N):
    M = int(f.readline())
    if(M < min['min']['value']):
      min['min'], min['min2'] = { 'value': M, 'index': i}, min['min']
    input.append(f.readline())

  C = []
  #정바향 호출
  min2 = input[min['min']['index']]
  minArr = input[min['min']['index']].split(" ")
  for i in range(0, len(minArr) - K + 1):
    candidate = " ".join(minArr[i:i+4])
    if(min2.find(candidate) != -1):
      C.append(candidate)
  
  minArr.reverse()
  for i in range(0, len(minArr) - K + 1):
    candidate = " ".join(minArr[i:i+4])
    if(min2.find(candidate) != -1):
      C.append(candidate)
  
  print(C)



  #역방향 호출

  
solution()





