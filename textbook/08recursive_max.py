# https://thebook.io/006935/part02/ch04/05-01/
# 4-2 문제 2의 숫자 n개 중에서 최댓값 찾기를 재귀 호출로 만들어 보세요.


def recursive_max(a, num):
    if(len(a) == 0):
        return num
    return recursive_max(a[1:len(a)], max(num, a[0]))


print(recursive_max([1, 5, 6, 9, 2, 8, 3], 0))
