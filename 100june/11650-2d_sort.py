import sys
read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
li = []
for _ in range(N):
  x, y = map(int, read().split(' '))
  li.append((x, y))
li.sort()
for x, y in li:
  write(str(x) + ' ' + str(y))