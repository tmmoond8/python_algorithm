# https://thebook.io/006935/part03/ch11/
# 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘을 만들어 보세요.


def partition(arr):
    if(len(arr) == 1):
        return ([], arr, [])
    lower = []
    higher = []
    pivot = arr.pop()
    for i in range(0, len(arr)):
        if pivot < arr[i]:
            higher.append(arr[i])
        else:
            lower.append(arr[i])
    return (lower, [pivot], higher)


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    (lower, pivot, higher) = partition(arr)
    return quick_sort(lower) + pivot + quick_sort(higher)


print(quick_sort([4, 6, 1, 9, 8, 2, 3, 2, 6, 7]))
