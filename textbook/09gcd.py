# https://thebook.io/006935/part02/ch05/
# 두 자연수 a와 b의 최대공약수를 구하는 알고리즘을 만들어 보세요.


def gcd(a, b):
    if(a < b):
        big = b
        small = a
    else:
        big = a
        small = b
    if(small == 0):
        return big
    return gcd(small, big % small)


print(12 % 7)
print(gcd(192, 72))
print(gcd(60, 48))
