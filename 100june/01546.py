import sys
def solve(N, data):
  N = int(N)
  arr = map(int, data.split(" "))
  sum = 0
  maxValue = 0
  for item in arr:
    sum += item
    maxValue = max(maxValue, item)

  return (format(sum / maxValue * 100 / N, '.3f'))[:-1]

print(solve(sys.stdin.readline(), sys.stdin.readline()))
# print(solve("3", "40 80 60") == "75.00")
# print(solve("3", "10 20 30") == "66.66")
# print(solve("4", "1 100 100 100") == "75.25")
# print(solve("5", "1 2 4 8 16") == "38.75")
# print(solve("2", "3 10") == "65.00")