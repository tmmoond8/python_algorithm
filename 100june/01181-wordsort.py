import sys

def solution():
  N = int(sys.stdin.readline().strip())
  dico = [ []* i for i in range(1, 51)]
  for i in range(0, N):
    word = sys.stdin.readline().strip()
    length = len(word)
    dico[length - 1].append(word)
  for i in dico:
    if len(i) > 0:
      i = list(set(i))
      i.sort()
      for k in i:
        print(k)

solution()