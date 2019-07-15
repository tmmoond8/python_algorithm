# https://thebook.io/006935/part03/ch11/05-01/
# 11-1 지금까지 배운 네 가지 정렬 알고리즘 말고도 훨씬 많은 정렬 알고리즘이 있습니다. 그 중 하나인 거품 정렬(Bubble sort)을 줄 서기로 비유하면 다음과 같습니다.
# 다음 과정을 읽고 리스트 [2, 4, 5, 1, 3]이 정렬되는 과정을 알고리즘으로 적어 보세요.


def bubble_sort(a):
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if(a[j] < a[i]):
                a[i], a[j] = a[j], a[i]
    return a


print(bubble_sort([1, 5, 6, 8, 3, 4, 2, 7, 4, 1]))
