import sys

# N = int(sys.stdin.readline().strip())
# street = list(map(int, sys.stdin.readline().strip().split(' ')))

def highest(street):
    MAX = 0
    prev = street[0]
    y, d, s = 0, 0, 0
    for i in range(1, len(street)):
        c = street[i]
        if c < prev:
            y = 0
            d = 0
            prev = c
            s = 0
            continue
        if d != c - prev:
            s = s +  d * y
            d = c - prev
            y = 0
        if d == 0:
            s = 0
            continue
        y += 1
        MAX = max(MAX, s + d * y)
        prev = c
    print(MAX)

# highest(street);
highest([12, 20, 1, 3, 4, 11, 1])
# highest([8, 1, 3, 4, 6, 7, 8, 1, 2, 3, 4, 5, 7, 2, 4, 5, 6, 7])