def solution():
  f = open(__file__.split('.')[0] + "-input.txt", 'r')
  src = f.readline()
  target = f.readline()
  srcIndex, srcLength = 0, len(src)
  targetIndex, targetLength = 0, len(target)
  noneHit = False
  distance = 0
  while(srcIndex < srcLength or targetIndex < targetLength):
    if(src[srcIndex] == targettargetIndex]):
      srcIndex += 1
      targetIndex += 1
      if(noneHit):
        distance += 1
        noneHit = False
    else:
      noneHit = True

solution()