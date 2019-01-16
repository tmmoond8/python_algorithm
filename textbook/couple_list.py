def couple_list(a):
  L = len(a)
  for i in range(0, L - 1):
    for j in range(i + 1, L):
      print(a[i] + ' - ' + a[j])

couple_list(["Tom", "Jerry", "Mike"])
couple_list(["Tom", "Jerry", "Mike", "Nami"])