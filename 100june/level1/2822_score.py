import sys

scores = []
for i in range(0, 8):
    scores.append(int(sys.stdin.readline().strip()))

def scoreSum(scores):
    tuple = []
    for i in range(0, len(scores)):
        tuple.append((i + 1, scores[i]))
    tuple.sort(key = lambda element : -element[1])
    top = []
    sum = 0
    for j in range(0, 5):
        sum += tuple[j][1]
        top.append(str(tuple[j][0]))
    print(sum)
    top.sort()

    print(" ".join(top))

scoreSum(scores)