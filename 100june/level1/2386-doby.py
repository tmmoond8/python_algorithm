import sys

def counter(str, c):
    return str.lower().count(c)

while True:
    line = sys.stdin.readline().strip()
    if line == '#':
        break
    p = line.split(' ')
    c = p.pop(0)
    print(c + ' ' + str(counter(' '.join(p), c)))
