def quick_sort(a):
  if(len(a) < 2):
    return a
  mid = len(a) // 2
  midValue = a[mid]
  a.pop(mid)
  upper = []
  lower = []
  for i in range(0, len(a)):
    if(a[i] > midValue):
      upper.append(a[i])
    else:
      lower.append(a[i])
  a1 = quick_sort(lower)
  a2 = quick_sort(upper)
  return a1 + [midValue] + a2

print(quick_sort([4, 6, 1, 9, 8, 2, 3, 2, 6, 7]))