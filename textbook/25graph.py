# https://thebook.io/006935/part04/ch15/06-03/
# 15-1 문제 15에서 배운 그래프 탐색 알고리즘을 이용하여 다음 그래프를 탐색하는 프로그램을 만들어 보세요(시작 꼭짓점: 1).
def tree_search(a, s, x):
    qu = []
    qu.append(("root", s))
    while (qu):
        (b, y) = qu.pop(0)
        print(b + '->' + y)
        if (y == x):
            print('found!!')
            return
        for c in a[y]:
            qu.append((y, c))
    print("not found!")


graph_info = {
    "1": ["2", "3"],
    "2": ["4", "5"],
    "3": [],
    "4": [],
    "5": [],
}

tree_search(graph_info, "1", "4")