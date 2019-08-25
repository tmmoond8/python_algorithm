import sys

def count_vowel(str):
    lower = str.lower()
    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    
    length = len(lower)
    for i in range(0, length):
        if(lower[i] in vowel):
            count += 1

    return count

while(True):
    text = sys.stdin.readline().strip()
    if text == '#':
        break
    print(count_vowel(text))
