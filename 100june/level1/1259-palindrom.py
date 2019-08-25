import sys

def my_palindrome(str):
    length = len(str)
    for i in range(0, length):
        if(str[i] != str[length - 1 - i]):
            return "no"

    return "yes"

while(True):
    text = sys.stdin.readline().strip()
    if text == '0':
        break
    print(my_palindrome(text))

