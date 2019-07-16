# https://thebook.io/006935/part05/ch16/01-01/
# 일단 미로를 풀려면 미로 안의 공간을 정형화해야 합니다. 그림 16-1의 퍼즐은 4×4로 구성된 간단한 미로입니다.
# 먼저 이동 가능한 위치를 각각의 구역으로 나누고, 구역마다 알파벳으로 이름을 붙이면 그림 16-2와 같습니다.
# 참고 이미지 https://thebook.io/img/006935/159.jpg


def maze_runner(maze, passed, start, end):
    print(passed)
    passed = list(passed)
    if (start == end):
        print('found !!', passed + [end])
    candidate = maze[start]
    passed.append(start)
    for c in candidate:
        if (c not in passed):
            maze_runner(maze, passed, c, end)


def maze_runner2(maze, passed, start, end):
    if start == end:
        print(passed + [end])
        return
    next = maze[start]
    for n in next:
        if n not in passed:
            maze_runner(maze, passed + [start], n, end)


maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}

maze_runner(maze, [], 'a', 'p')