def descendingOrder(a, b):
  return a > b

def ascendingOrder(a, b):
  return a < b

def selection_sort(a, compare):
  for i in range(0, len(a) - 1):
    minIndex = i
    for j in range(i + 1, len(a)):
      if(compare(a[j], a[minIndex])):
        minIndex = j
    a[i], a[minIndex] = a[minIndex], a[i]
    print(a)
  print('---------------------')
  return a


a1 = [1, 5, 7, 9, 4, 5, 2, 8]
a2 = [1, 5, 7, 9, 4, 5, 2, 8]
# print(swap(a1, 3, 6))
# swap(a1, 3, 6)
selection_sort(a1, ascendingOrder)
selection_sort(a2, descendingOrder)