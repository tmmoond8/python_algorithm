import sys

def bubble(woods):
    for i in range(0, 4):
        if (woods[i] > woods[i + 1]):
            woods[i], woods[i+1] = woods[i+1], woods[i]
            print(' '.join(woods))

woods = list(map(str, sys.stdin.readline().strip().split(' ')))

for j in range(0, 4):
    bubble(woods)