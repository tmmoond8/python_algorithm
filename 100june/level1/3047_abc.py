import sys

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
arr.sort()

ABC = { 'A': arr[0], 'B': arr[1],'C': arr[2]}
abc = sys.stdin.readline().strip()

output = []
for i in range(0, 3):
    output.append(ABC[abc[i]])
print(output[0], output[1], output[2])
# print(' '.join(str(output)))

# print(arr)
# print(' '.join(arr))
# print(ABC['A'])