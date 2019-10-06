import sys

N = int(sys.stdin.readline().strip())

vote = list(map(str, sys.stdin.readline().strip()))

A_count = 0
B_count = 0

for i in range(0, N):
    if vote[i] == 'A':
        A_count += 1
    else:
        B_count += 1
if A_count == B_count:
    print('Tie')
elif A_count > B_count:
    print('A')
else:
    print('B')