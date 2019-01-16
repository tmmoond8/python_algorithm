def same_name(a):
  s = set()
  l = len(a)
  for i in range(0, l - 1):
    for j in range(i + 1, l):
      if(a[i] == a[j]):
        s.add(a[i])
  return s
print(same_name(["Tom", "Jerry", "Mike", "Tom"]))