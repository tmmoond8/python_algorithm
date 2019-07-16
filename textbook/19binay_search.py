# https://thebook.io/006935/part03/ch12/
# 자료가 크기 순서대로 정렬된 리스트에서 특정한 값이 있는지 찾아 그 위치를 돌려주는 알고리즘을 만들어 보세요. 리스트에 찾는 값이 없으면 -1을 돌려줍니다.


def recursive_search(a, value, pos):
    if(a[pos] == value):
        return pos
    if(len(a) == 1 and a[0] != value):
        return -100000
    elif(a[pos] < value):
        upper = a[pos + 1:]
        return pos + recursive_search(upper, value, len(upper) // 2) + 1
    elif(a[pos] > value):
        lower = a[:pos]
        return pos - (pos - recursive_search(lower, value, len(lower) // 2))


def binay_search(a, value, pos):
    result = recursive_search(a, value, pos)
    return result < 0 and -1 or result


a1 = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binay_search(a1, 36, len(a1)//2))
print(binay_search(a1, 1, len(a1)//2))
print(binay_search(a1, 4, len(a1)//2))
print(binay_search(a1, 9, len(a1)//2))
print(binay_search(a1, 16, len(a1)//2))
print(binay_search(a1, 10, len(a1)//2))
print(binay_search(a1, 100, len(a1)//2))
