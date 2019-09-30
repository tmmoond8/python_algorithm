import sys, math

def splitt(number):
    if number % 2 == 0:
        return math.floor((number / 2) * (number / 2))
    else:
        return math.floor(((number + 1) / 2) * ((number + 1) / 2) - ((number + 1) / 2))

N = int(sys.stdin.readline().strip())
print(splitt(N + 2))

# print(math.floor(splitt(1)))
# print(math.floor(splitt(2)))
# print(math.floor(splitt(3)))
# print(math.floor(splitt(4)))
# print(math.floor(splitt(5)))

# 0 -> 0 -> 1
# 1 -> 0 -> 2
# 2 -> 1 -> 4
# 3 -> 2 ->  6
# 4 -> 4 -> 9
# 5 -> 6 -> 12
# 6 -> 9 -> 16
# 7 -> 12 -> 20
# 8 -> 16
# 9 -> 20
# 10 -> 25
# 1 1 2 2 3 3 4 4 5 5 6 6
