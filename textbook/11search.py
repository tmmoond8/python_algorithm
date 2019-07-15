# https://thebook.io/006935/part03/ch07/
# 주어진 리스트에 특정한 값이 있는지 찾아 그 위치를 돌려주는 알고리즘을 만들어 보세요. 리스트에 찾는 값이 없다면 -1을 돌려줍니다.


def search(a, x):
    pos = -1
    for i in range(0, len(a)):
        if(x == a[i]):
            pos = i
            break
    return pos


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search(v, 18))
print(search(v, 33))
print(search(v, 900))
