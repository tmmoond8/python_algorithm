# 1부터 n까지 연속한 정수의 합을 구하는 알고리즘을 만들어 보세요.
# 1부터 10까지의 수를 모두 더하면? 55
# 1부터 100까지의 수를 모두 더하면? 5050


def sum_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


print(sum_n(100))
