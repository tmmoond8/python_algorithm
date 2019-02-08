def brutal_earn_money(a):
  max = 0
  for i in range(0, len(a)):
    for j in range(i +1, len(a)):
      if(max < a[j] - a[i]):
        max = a[j] - a[i]
  return max

def earn_money1(a):
  ac = list(a)
  i = max = 0
  length = 0
  while(i < len(ac) - 1):
    for j in range(i + 1, len(ac)):
      if(ac[j] < ac[i]):
        i = j
        break
      elif(max < ac[j] - ac[i]):
        max = ac[j] - ac[i]
      if(j == len(ac) - 1):
        i = j
  print(max)
    

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

print(brutal_earn_money(stock))
earn_money1(stock)