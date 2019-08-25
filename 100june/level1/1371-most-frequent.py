import sys

S = sys.stdin.read()

length = len("".join(S))
dic = {}
for code in range(ord('a'), ord('z') + 1):
    dic[chr(code)] = 0

for i in range(0, length):
    if S[i].isalpha():
        dic[S[i]] += 1

MAX = 0
for code in range(ord('a'), ord('z') + 1):
    MAX = max(MAX, dic[chr(code)])
    
mfa = []
for code in range(ord('a'), ord('z') + 1):
    if dic[chr(code)] == MAX:
        mfa.append(chr(code))
print("".join(mfa))