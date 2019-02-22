import sys
read = sys.stdin.readline

N = int(read())

L = [i for i in range(1, N + 1)]
counter = i = 0

while counter < N - 1:
  if i % 2 != 0:
    L.append(L[i])
    counter += 1
  i += 1

print(L.pop())