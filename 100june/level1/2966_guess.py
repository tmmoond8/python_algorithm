import sys

def adrian(arr):
    SHEET = ['A', 'B', 'C']
    SHEET_SIZE = len(SHEET)
    sum = 0
    for i in range(len(arr)):
        if arr[i] == SHEET[i % SHEET_SIZE]:
            sum += 1
    return sum

def bruno(arr):
    SHEET = ['B', 'A', 'B', 'C']
    SHEET_SIZE = len(SHEET)
    sum = 0
    for i in range(len(arr)):
        if arr[i] == SHEET[i % SHEET_SIZE]:
            sum += 1
    return sum

def goran(arr):
    SHEET = ['C', 'C', 'A', 'A', 'B', 'B']
    SHEET_SIZE = len(SHEET)
    sum = 0
    for i in range(len(arr)):
        if arr[i] == SHEET[i % SHEET_SIZE]:
            sum += 1
    return sum

N = int(sys.stdin.readline().strip())
ARR = sys.stdin.readline().strip()

# Adrian
# Bruno
# Goran

A = adrian(ARR)
B = bruno(ARR)
G = goran(ARR)

MAX = max(A, max(B, G))
print(MAX)
if MAX == A:
    print('Adrian')
if MAX == B:
    print('Bruno')
if MAX == G:
    print('Goran')
    