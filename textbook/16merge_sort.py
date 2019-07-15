# https://thebook.io/006935/part03/ch10/
# 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘을 만들어 보세요.


def merge(a, b):
    aLen = len(a)
    bLen = len(b)
    aIdx = 0
    bIdx = 0
    merged = []

    for i in range(0, aLen + bLen):
        if aLen == aIdx:
            merged.append(b[bIdx])
            bIdx += 1
        elif bLen == bIdx:
            merged.append(a[aIdx])
            aIdx += 1
        elif a[aIdx] < b[bIdx]:
            merged.append(a[aIdx])
            aIdx += 1
        else:
            merged.append(b[bIdx])
            bIdx += 1
    return merged


def merge_sort(arr):
    if(len(arr) == 1):
        return arr
    a = merge_sort(arr[:len(arr)//2])
    b = merge_sort(arr[len(arr)//2:])
    return merge(a, b)


a = [1, 3, 8, 5, 2, 6, 3, 4, 3]
print(merge_sort(a))
