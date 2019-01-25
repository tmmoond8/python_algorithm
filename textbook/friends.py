def all_friends(a, name):
  qu = list(a[name])
  done = set()
  while(qu):
    item = qu.pop()
    done.add(item)
    for i in a[item]:
      if(i not in done):
        qu.append(i)
  return done

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