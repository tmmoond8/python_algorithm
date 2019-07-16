# https://thebook.io/006935/part04/ch14/02-02/
# 딕셔너리를 이용해 동명이인을 찾는 알고리즘


def samename2(a):
    d = dict()
    s = set()
    for i in a:
        if (i in d):
            d[i] += 1
            s.add(i)
        else:
            d[i] = 1
    return s


print(samename2(["Tom", "Eric", "Jerry", "Tom"]))
