def search(a, x):
  pos = -1
  for i in range(0, len(a)):
    if(x == a[i]):
      pos = i
      break
  return pos

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search(v, 18))
print(search(v, 33))
print(search(v, 900))