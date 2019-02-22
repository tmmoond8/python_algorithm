import sys
read = sys.stdin.readline
# data = """
# 10 4790
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000
# """
# data = list(filter(lambda l: len(l) > 0, data.split('\n')))
# D, Res = map(int, data.pop(0).split(' '))
D, Res = map(int, read().rstrip().split(' '))
data = []
for _ in range(D):
  data.append(read().rstrip())
MONEY = list(map(int, data))
MONEY.reverse()
MIN = Res

q = []

q.append((0, Res, 0))
minn = Res
while q:
  i, y, x = q.pop()
  if(y == 0):
    minn = min(minn, x)
    q.clear()
    continue
  if(x >= minn or i >= D):
    continue
  
  value = y // MONEY[i]
  q.append((i + 1, y - MONEY[i]*value, x + value))
    
  
print(minn)