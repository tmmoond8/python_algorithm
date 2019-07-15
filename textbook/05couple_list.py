# https://thebook.io/006935/part01/ch03/03-02/
# 3-1 n명 중 두 명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘을 만들어 보세요.


def couple_list(a):
    L = len(a)
    for i in range(0, L - 1):
        for j in range(i + 1, L):
            print(a[i] + ' - ' + a[j])


couple_list(["Tom", "Jerry", "Mike"])
couple_list(["Tom", "Jerry", "Mike", "Nami"])
