def tree_search(a, s, x):
  qu = []
  qu.append(("root", s))
  while(qu):
    (b, y) = qu.pop(0)
    print(b + '->' +y)
    if(y == x):
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