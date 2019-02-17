f = open("100june/01230-input.txt", "r")
while(True):
  try:
    b = input()
    print(b)
    
  except EOFError:
    break