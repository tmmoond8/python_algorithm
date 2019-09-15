import sys

numList = []
for i in range(0, 7):
    numList.append(int(sys.stdin.readline().strip()))

def oddsum(arr):
    oddSum, oddMin = 0, 100
    for i in range(0, 7):
        if arr[i] % 2 == 1:
            oddSum += arr[i]
            oddMin = min(oddMin, arr[i])
    if oddSum == 0:
        print(-1)
        return
    print(oddSum)
    print(oddMin)

oddsum(numList)