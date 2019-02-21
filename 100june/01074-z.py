import sys
N, Y, X = map(int, sys.stdin.readline().strip().split(' '))

def z(left, top, n, sum):
  if(sum < -10):
    return 0
  if(left == X and top == Y):
    print(sum)
    return 1
  if(n == 1):
    return sum + 1
  half = n//2
  if(X < left + half and Y < top + half):
    sum = z(left, top, half, sum)
  elif(X >= left + half and Y < top + half):
    sum += half * half 
    sum += z(left + half, top, half, sum)
  elif(X < left + half and Y >= top + half):
    sum += 2 * half * half
    sum += z(left, top + half, half, sum)
  elif(X >= left + half and Y >= top + half):
    sum += 3 * half * half
    sum += z(left + half, top + half, half, sum)
  return sum


z(0, 0, pow(2, N), 0)