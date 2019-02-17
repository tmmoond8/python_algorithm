import sys
N = int(sys.stdin.readline())
num = sys.stdin.readline()
sum = 0
for i in range(0, N):
  sum += int(num[i])

print(sum)