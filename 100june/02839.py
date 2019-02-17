import sys
def solve(n):
  minValue = n
  coins = [5, 3]
  i = n // coins[0]
  while(i > -1):
    rest = n - i * coins[0]
    if(rest % coins[1] == 0):
      minValue = min(minValue, i + rest // coins[1])
    i += -1
  if(n == minValue):
    return -1
  else:
    return minValue

print(solve(int(sys.stdin.readline())))

# print(solve(18) == 4)
# print(solve(4) == -1)
# print(solve(6) == 2)
# print(solve(9) == 3)
# print(solve(11) == 3)