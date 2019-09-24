import sys, re

p = re.compile('([A-Z*0-9*-])+')

def fbi(name):
    if (p.match(name) == None):
        return False
    return "FBI" in name

I = []
for i in range(0, 5):
    if (fbi(sys.stdin.readline().strip())):
        I.append(str(i + 1))

if len(I) == 0 :
        print("HE GOT AWAY!")
else:
        print(" ".join(I))