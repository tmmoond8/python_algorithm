import sys, math

N = int(sys.stdin.readline())
arr = []

for i in range(0, N):
    arr.append(int(sys.stdin.readline()))

# N = 4
# arr = [364, 843, 1322, 1801]

hasCommonDifference = arr[1] - arr[0] == arr[2] - arr[1]
if hasCommonDifference:
    commonDifference = arr[1] - arr[0]
    print(arr[0] + N * commonDifference)
else:
    commonRatio = arr[1] / arr[0]
    print(arr[0] * math.floor(math.pow(commonRatio, N)))