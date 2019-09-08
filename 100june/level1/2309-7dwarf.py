import sys

dwarf = []
for i in range(0, 9):
    dwarf.append(int(sys.stdin.readline().strip()))

total = sum(dwarf)
rest = total - 100
dwarf.sort()
a, b = -1, -1
for i in range(0, 9):
    for j in range(0, 9):
        if i != j and rest == dwarf[i] + dwarf[j]:
            a, b = i, j
            break

dwarf.pop(a)
dwarf.pop(b)
for i in range(0, 7):
    print(dwarf[i])
