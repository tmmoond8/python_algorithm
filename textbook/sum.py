def sum_n(n):
  sum = 0
  for i in range(1, n + 1):
    sum += i
  return sum

print(sum_n(100))