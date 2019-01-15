def max_num(a):
  max = 0
  pos = -1
  for i in range(0, len(a)):
    if a[i] > max:
      max = a[i]
      pos = i
  return max

def max_pos(a):
  max = 0
  pos = -1
  for i in range(0, len(a)):
    if a[i] > max:
      max = a[i]
      pos = i
  return pos
  
def min_num(a):
  min = 10000
  for i in range(1, len(a)):
    if (a[i] < min):
      min = a[i]
  return min

print(max_num([17, 92, 18, 33, 58, 7, 33, 42]))
print(max_pos([17, 92, 18, 33, 58, 7, 33, 42]))
print(min_num([17, 92, 18, 33, 58, 7, 33, 42]))