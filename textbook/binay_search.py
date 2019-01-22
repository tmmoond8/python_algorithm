def binay_search(a, value, pos):
    if(a[pos] == value):
      return pos
    if(len(a) == 1 and a[0] != value):
      return -100000
    elif(a[pos] < value):
      upper = a[pos + 1:]
      return pos + binay_search(upper, value, len(upper) // 2) + 1
    elif(a[pos] > value):
      lower = a[:pos]
      return pos - (pos - binay_search(lower, value, len(lower) // 2))

a1 = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binay_search(a1, 36, len(a1)//2))
print(binay_search(a1, 1, len(a1)//2))
print(binay_search(a1, 4, len(a1)//2))
print(binay_search(a1, 9, len(a1)//2))
print(binay_search(a1, 16, len(a1)//2))
print(binay_search(a1, 10, len(a1)//2))
print(binay_search(a1, 100, len(a1)//2))