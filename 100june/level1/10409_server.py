import sys

N, T = map(int, sys.stdin.readline().strip().split(' '))
S = list(map(int, sys.stdin.readline().strip().split(' ')))

# N = 10
# T = 200
# S = [20, 7, 10, 8, 10, 27, 2, 3, 10, 5]

def solve(n, t, s):
    rest = t
    for i in range(n + 10):
        if i == n:
            break
        if rest >= s[i]:
            rest -= s[i]
        else:
            break
    return i
print(solve(N, T, S))