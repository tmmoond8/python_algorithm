import sys
k = sys.stdin.readline().strip().split(' ')

def sage(k):
    minValue = 10000
    for i in range(0, 4):
        minValue = min(minValue, int("".join(k[i: 4] + k[0: i])))
    return minValue

minValue = sage(k)

index = 0
j = 1111
while j <= minValue:
    if '0' not in str(j) and j == sage(list(str(j))):
        index += 1
    j += 1
print(index)