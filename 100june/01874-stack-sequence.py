import sys
read = sys.stdin.readline    

from random import shuffle
data = []
for i in range(1, 10001):
  data.append(str(i))
shuffle(data)

# data = """
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1
# 9
# 10
# """.split('\n')
N = 10000
data = list(filter(lambda l: len(l) > 0, data))
# N = int(read())
# data = []
# for _ in range(N):
#   data.append(read().rstrip())
# def solution(i, pop, push, history):
#   if not ','.join(data).startswith(','.join(pop)):
#     return
#   if(i > N):
#     push.reverse()
#     if ','.join(data) == ','.join(pop + push):
#       history += '-'*len(push)
#       print('\n'.join(list(history)))
#       sys.exit(1)
#     else:
#       return
#   if len(push) > 0:
#     solution(i, pop + push[-1:], push[:-1], history + '-')
#   solution(i + 1, pop, push + [str(i)], history + '+')
#   return

q = []
q.append((1, [], [], ''))

while(q):
  i, pop, push, history = q.pop(0)
  if not ','.join(data).startswith(','.join(pop)):
    continue
  if(i > N):
    push.reverse()
    if ','.join(data) == ','.join(pop + push):
      history += '-'*len(push)
      print('\n'.join(list(history)))
      sys.exit(1)
    else:
      continue
  if len(push) > 0:
    q.append((i, pop + push[-1:], push[:-1], history + '-'))
  q.append((i + 1, pop, push + [str(i)], history + '+'))

print('NO')
