# https://thebook.io/006935/part02/ch04/05-01/
# 4-1 문제 1의 1부터 n까지의 합 구하기를 재귀 호출로 만들어 보세요.


def recursive_sum(n):
    if(n == 1):
        return 1
    return n + recursive_sum(n - 1)


print(recursive_sum(10))
