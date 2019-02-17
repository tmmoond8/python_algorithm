import sys
inputStr = sys.stdin.readline()
buffer = []
for i in range(0, len(inputStr)):
  buffer.append(inputStr[i])
  if(i % 10 == 9):
    print("".join(buffer))
    buffer.clear()
if(len(buffer) != 0):
  print("".join(buffer))