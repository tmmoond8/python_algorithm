import sys
def solve(inputLine):
  E, S, M = map(int, inputLine.split(" "))
  e = s = m = i = 1
  while(True):
    if(E == e and S == s and M == m):
      return i
    else:
      e, s, m, i = e + 1, s + 1, m + 1, i + 1
      if(e == 16):
        e = 1
      if(s == 29):
        s = 1
      if(m == 20):
        m = 1

print(solve(sys.stdin.readline()))

# print(solve("1 16 16") == 16)
# print(solve("1 1 1") == 1)
# print(solve("1 2 3") == 5266)
# print(solve("15 28 19") == 7980)