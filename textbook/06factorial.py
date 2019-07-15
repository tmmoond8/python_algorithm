# https://thebook.io/006935/part02/ch04/
# 1부터 n까지 연속한 정수의 곱을 구하는 알고리즘을 만들어 보세요.


def factorial(n):
    if(n == 1):
        return 1
    return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
