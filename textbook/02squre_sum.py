# https://thebook.io/006935/part01/ch01/06-02/
# 1-1 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for 반복문으로 만들어 보세요
# (예를 들어 n = 10이라면 12 + 22 +32 + … + 102 = 385를 계산하는 프로그램입니다).


def squre_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum


print(squre_sum(10))
