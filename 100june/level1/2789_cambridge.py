import sys, re

def remove_cambridge(str):
    ban = set(['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E'])
    idx = 0
    strArr = list(str)
    while idx < len(strArr):
        if strArr[idx] in ban:
            strArr.pop(idx)
        else:
            idx += 1
    return ''.join(strArr)

inputStr = sys.stdin.readline().strip()
print(remove_cambridge(inputStr))