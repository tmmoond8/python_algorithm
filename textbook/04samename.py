# https://thebook.io/006935/part01/ch03/
# n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘을 만들어 보세요.


def same_name(a):
    s = set()
    l = len(a)
    for i in range(0, l - 1):
        for j in range(i + 1, l):
            if (a[i] == a[j]):
                s.add(a[i])
    return s


print(same_name(["Tom", "Jerry", "Mike", "Tom"]))
