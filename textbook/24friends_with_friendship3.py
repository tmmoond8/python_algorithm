# 임의의 문제 입니다.
# a - b, c 1
#   - d    2
#   - e    3


def all_friends(fr_info, target):
    level = 0
    friendShip = {level: [target]}
    done = set()
    done.add(target)
    while len(friendShip[level]) > 0:
        next = friendShip[level]
        level += 1
        friendShip[level] = []
        for i in next:
            for j in fr_info[i]:
                if j not in done:
                    friendShip[level].append(j)
                    done.add(j)
    return friendShip


fr_info = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["b"],
    "d": ["c", "e"],
    "e": []
}
print(all_friends(fr_info, "a"))