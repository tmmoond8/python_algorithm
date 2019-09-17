import sys

def switch_case(str):
    originStr = list(str)
    switched = []
    for i in range(0, len(originStr)):
        if originStr[i].islower():
            switched.append(originStr[i].upper())
        else:
            switched.append(originStr[i].lower())
    return ''.join(switched)

str = sys.stdin.readline().strip()

print(switch_case(str))