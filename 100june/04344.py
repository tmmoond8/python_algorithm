import sys
def solve():
  f = open(__file__[:-2] + 'input', "r")
  N = int(f.readline())
  for i in range(0, N):
    data = [ int (i) for i in f.readline().split(" ") ]
    n = int(data.pop(0))
    average = sum(data) / n
    over = 0
    for j in range(0, n):
      if(data[j] > average):
        over += 1
    print("{0:.3f}%".format(over/n*100))

solve()
