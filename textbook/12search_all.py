# https://thebook.io/006935/part03/ch07/02-01/
# 7-1 프로그램 7-1은 리스트에 찾는 값이 여러 개 있더라도 첫 번째 위치만 결과로 돌려줍니다. 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 탐색 알고리즘을 만들어 보세요.
# 찾는 값이 리스트에 없다면 빈 리스트인 [ ]를 돌려줍니다.


def search_all(a, x):
    pos = []
    for i in range(0, len(a)):
        if(x == a[i]):
            pos.append(i)
    return pos


print(search_all([1, 4, 6, 2, 4, 1, 2, 3, 4, 2, 1, 2], 1))
