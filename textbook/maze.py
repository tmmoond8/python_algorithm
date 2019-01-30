def maze_runner(maze, passed, start, end):
  print(passed)
  passed = list(passed)
  if(start == end):
    print('found !!', passed + [end])
  candidate = maze[start]
  passed.append(start)
  for c in candidate:
    if(c not in passed):
      maze_runner(maze, passed, c, end)

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