def find_coin(a, start, end):
  lower = upper = 0
  i = start
  mid = (start + end) // 2
  for i in range(start, mid + (start + end) % 2):
    lower += a[i]
  for i in range(mid + 1, end + 1):
    upper += a[i]
  
  if(lower == upper):
    return mid
  elif(lower < upper):
    if(end - start < 3):
      return start
    return find_coin(a, start, mid)
  else :
    if(end - start < 3):
      return end
    return find_coin(a, mid + 1, end)

coins = [ 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6]

print(find_coin([ 6, 6, 6, 5, 6, 6], 0, len([ 6, 6, 6, 5, 6, 6]) - 1))     # 3
print(find_coin([ 6, 6, 6, 6, 6, 5], 0, len([ 6, 6, 6, 6, 6, 5]) - 1))     # 5
print(find_coin([ 6, 6, 6, 6, 5, 6], 0, len([ 6, 6, 6, 6, 5, 6]) - 1))     # 4
print(find_coin([ 6, 5, 6, 6, 6, 6], 0, len([ 6, 5, 6, 6, 6, 6]) - 1))     # 1
print(find_coin([ 6, 5, 6, 6, 6], 0, len([ 6, 5, 6, 6, 6]) - 1))     # 1
print(find_coin([ 6, 6, 6, 5, 6], 0, len([ 6, 6, 6, 5, 6]) - 1))     # 3
print(find_coin(coins, 0, len(coins) - 1))     #  17