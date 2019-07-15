# https://thebook.io/006935/part03/ch09/
# 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘을 만들어 보세요.


def ascendingOrder(a, b):
    return a < b


def descendingOrder(a, b):
    return not ascendingOrder(a, b)


def insertion_sort(a, compare):
    size = len(a)
    sorted = []
    for i in range(0, size):
        item = a.pop()
        for j in range(0, i):
            if(compare(sorted[j], item)):
                sorted.insert(j, item)
                break
        if item not in sorted:
            sorted.append(item)
    print(sorted)
    print("----------")
    return a


a1 = [1, 5, 7, 9, 4, 5, 2, 8]
a2 = [1, 5, 7, 9, 4, 5, 2, 8]

insertion_sort(a1, ascendingOrder)
insertion_sort(a2, descendingOrder)
