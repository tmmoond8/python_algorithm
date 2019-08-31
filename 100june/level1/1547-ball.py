import sys

def switch(a, b):
    cups[a], cups[b] = cups[b], cups[a]

cups = [-1, 1, 0, 0];
changeList = []

N = int(sys.stdin.readline())
for i in range(0, N):
    a, b = map(int, sys.stdin.readline().split(" "))
    switch(a, b)

for i in range(0, len(cups)):
    if cups[i] == 1:
        print(i)

