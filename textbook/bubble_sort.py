def bubble_sort(a):
  for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
      if(a[j] < a[i]):
        a[i], a[j] = a[j], a[i]
  return a

print(bubble_sort([1, 5, 6, 8, 3, 4, 2, 7, 4, 1]))