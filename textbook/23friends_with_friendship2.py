# https://thebook.io/006935/part04/ch15/06-01/
# 모든 친구를 찾아서 친밀도를 계산하는 알고리즘
def all_friends(a, name):
    done = set()
    qu = []
    done.add(name)
    qu.append((name, 0))
    while (qu):
        (name, level) = qu.pop(0)
        print(name, level)
        for k in a[name]:
            if (k not in done):
                done.add(k)
                qu.append((k, level + 1))


fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

all_friends(fr_info, 'Summer')
print()
all_friends(fr_info, 'Jerry')