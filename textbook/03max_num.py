# https://thebook.io/006935/part01/ch02/
# 주어진 숫자 n개 중 가장 큰 숫자를 찾는 알고리즘을 만들어 보세


def max_num(a):
    max = 0
    pos = -1
    for i in range(0, len(a)):
        if a[i] > max:
            max = a[i]
            pos = i
    return max


def max_pos(a):
    max = 0
    pos = -1
    for i in range(0, len(a)):
        if a[i] > max:
            max = a[i]
            pos = i
    return pos


def min_num(a):
    min = 10000
    for i in range(1, len(a)):
        if (a[i] < min):
            min = a[i]
    return min


array = [17, 92, 18, 33, 58, 7, 33, 42, 102]
print(max_num(array))
print(max_pos(array))
print(min_num(array))
