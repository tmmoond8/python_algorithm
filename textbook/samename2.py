def samename2(a):
  d = dict()
  s = set()
  for i in a:
    if(i in d):
      d[i] += 1
    else:
      d[i] = 1
  for j in d:
    if(d[j] > 1):
      s.add(j)
  return s

print(samename2(["Tom", "Eric", "Jerry", "Tom"]))