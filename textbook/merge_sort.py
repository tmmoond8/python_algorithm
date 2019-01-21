
def merge(a, b):
  aIndex = bIndex = 0
  lenA = len(a)
  lenB = len(b)
  m = []
  for i in range(0, lenA + lenB):
    if(bIndex >= lenB):
      m.append(a[aIndex])
      aIndex += 1
    elif (aIndex >= lenA):
      m.append(b[bIndex])
      bIndex += 1
    elif(b[bIndex] < a[aIndex]):
      m.append(b[bIndex])
      bIndex += 1
    elif(a[aIndex] < b[bIndex]):
      m.append(a[aIndex])
      aIndex += 1
    else:
      m.append(a[aIndex])
      aIndex += 1
  return m

def merge_sort(a):
  if(len(a) <= 1):
    return a
  a1 = merge_sort(a[:len(a)//2])
  a2 = merge_sort(a[len(a)//2:])
  return merge(a1, a2)

a = [1, 3, 8, 5, 2, 6, 3, 4, 3]
print(merge_sort(a))