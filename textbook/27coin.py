# https://thebook.io/006935/part05/ch17/
# 겉보기에는 똑같은 동전이 n개 있습니다. 이 중에서 한 개는 싸고 가벼운 재료로 만들어진 ‘가짜 동전’입니다.
# 좌우 무게를 비교할 수 있는 양팔 저울을 이용해서 다른 동전보다 가벼운 가짜 동전을 찾아내는 알고리즘을 만들어 보세요.
def find_coin(a, start, end):
    lower = upper = 0
    i = start
    mid = (start + end) // 2
    for i in range(start, mid + (start + end) % 2):
        lower += a[i]
    for i in range(mid + 1, end + 1):
        upper += a[i]

    if (lower == upper):
        return mid
    elif (lower < upper):
        if (end - start < 3):
            return start
        return find_coin(a, start, mid)
    else:
        if (end - start < 3):
            return end
        return find_coin(a, mid + 1, end)


coins = [
    6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6,
    6, 6
]

print(find_coin([6, 6, 6, 5, 6, 6], 0, len([6, 6, 6, 5, 6, 6]) - 1))  # 3
print(find_coin([6, 6, 6, 6, 6, 5], 0, len([6, 6, 6, 6, 6, 5]) - 1))  # 5
print(find_coin([6, 6, 6, 6, 5, 6], 0, len([6, 6, 6, 6, 5, 6]) - 1))  # 4
print(find_coin([6, 5, 6, 6, 6, 6], 0, len([6, 5, 6, 6, 6, 6]) - 1))  # 1
print(find_coin([6, 5, 6, 6, 6], 0, len([6, 5, 6, 6, 6]) - 1))  # 1
print(find_coin([6, 6, 6, 5, 6], 0, len([6, 6, 6, 5, 6]) - 1))  # 3
print(find_coin(coins, 0, len(coins) - 1))  #  17
