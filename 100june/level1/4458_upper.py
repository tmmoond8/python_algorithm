import sys

N = int(sys.stdin.readline().strip())

for i in range(0, N):
    line = sys.stdin.readline().strip()
    print(line[0].upper() + line[1:])
