def ascendingOrder(a, b):
  return a < b

def descendingOrder(a, b):
  return not ascendingOrder(a, b)

def insertion_sort(a, compare):
  for i in range(0, len(a)):
    for j in range(0, i + 1):
      if(compare(a[i], a[j])):
        tmp = a[i]
        del a[i]
        a.insert(j, tmp)
    print(a)
  print("----------")
  return a

a1 = [1, 5, 7, 9, 4, 5, 2, 8]
a2 = [1, 5, 7, 9, 4, 5, 2, 8]

insertion_sort(a1, ascendingOrder)
insertion_sort(a2, descendingOrder)