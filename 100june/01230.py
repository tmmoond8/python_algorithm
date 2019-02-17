D = {}
def process(src, target):
  if(src == target):
    return 0
  if(src in D and target in D[src]):
    return D[src][target]
  target.split(src[0])
  
  
  return 4
def solution():
  f = open(__file__.split('.')[0] + "-input.txt", 'r')
  src = f.readline().replace('\n', '')
  target = f.readline().replace('\n', '')
  srcIndex, srcLength = 0, len(src)
  targetIndex, targetLength = 0, len(target)
  noneHit = False
  distance = 0

  return process(src, target)



  while(srcIndex < srcLength and targetIndex < targetLength):
    if(src[srcIndex] == target[targetIndex]):
      srcIndex += 1
      targetIndex += 1
      if(noneHit):
        distance += 1
        noneHit = False
    else:
      noneHit = True
      targetIndex += 1
  if(targetIndex != targetLength):
    distance += 1
  
  return distance


# print(solution())
# D['abc'] = { "ddd": 43}
print(D['abc']['ddd'])