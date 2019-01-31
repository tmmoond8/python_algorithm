def maze_runner(a, start, end):
  qu = []
  done = set()
  qu.append(start)

  while(qu):
    item = qu.pop(0)
    last = item[-1]
    done.add(item)
    if(last == end):
      return item
    for k in a[last]:
      if(item + k not in done):
        qu.append(item + k)


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

print(maze_runner(maze, 'a', 'p'))