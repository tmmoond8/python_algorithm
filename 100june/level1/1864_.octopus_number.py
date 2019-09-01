import sys, math

octMap = {
    "-": 0,
    "\\": 1,
    "(": 2,
    "@": 3,
    "?": 4,
    ">": 5,
    "&": 6,
    "%": 7,
    "/": -1
}

def parseOct(str):
    octArr = []
    lenth = len(str)
    for i in range(0, len(str)):
        octArr.append(octMap[str[lenth - 1 - i]])
    sum = 0
    for i in range(0, len(octArr)):
        sum += octArr[i] * math.pow(8, i)
    return math.floor(sum)

while True:
    l = sys.stdin.readline().strip()
    if l == '#':
        break
    print(parseOct(l))    

