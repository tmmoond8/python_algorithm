def search_all(a, x):
  pos = []
  for i in range(0, len(a)):
    if(x == a[i]):
      pos.append(i)
  return pos

print(search_all([1, 4, 6, 2, 4, 1, 2, 3, 4, 2,1 ,2], 1))