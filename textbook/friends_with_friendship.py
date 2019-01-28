import operator

def all_friends(a, name):
  level = 0
  done = dict()
  qu = dict()
  done[name] = level
  level += 1
  for i in a[name]:
    qu[i] = level
  
  for key in qu.keys():
    if(key not in done):
      done[key] = qu[key]

  while(len(qu.keys()) > 0):
    keys = qu.keys()
    key = list(keys)[0]
    if(key not in done):
      done[key] = qu[key]
    for k in a[key]:
      if(k not in done):
        qu[k] = done[key] + 1
    del qu[key]
  sortedArr = sorted(done.items(), key=operator.itemgetter(1))
  return sortedArr

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


print(all_friends(fr_info, 'Summer'))
print()
print(all_friends(fr_info, 'Jerry'))