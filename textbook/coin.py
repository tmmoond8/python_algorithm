def find_coin(a, start, end):
  lower = upper = 0
  i = start
  mid = (start + end) // 2
  while(i <= end):
    if((start + end) % 2 == 0 and i == mid):
      i += 1
      continue
    if(i <= mid):
      lower += a[i]
    else :
      upper += a[i]
    i += 1
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