import sys
# f = open(__file__.replace('.py', '.input'), 'r')
f = sys.stdin
board = []
for i in range(0, 9):
    row = list(map(int, f.readline().strip().split(' ')))
    board.append(row)

MAX, x, y = 0, -1, -1

for i in range(0, 9):
    for j in range(0, 9):
        if board[i][j] > MAX:
            MAX, x, y = board[i][j], i, j

print(MAX)
print(x + 1, y + 1)

f.close()