# https://thebook.io/006935/part04/ch13/02-01/
# 회문 찾기 알고리즘


def palindrome(str):
    qu = []
    st = []
    for x in str:
        if(x.isalpha()):
            qu.append(x.lower())
            st.append(x.lower())
    while qu:
        if(qu.pop(0) != st.pop()):
            return False
    return True


def my_palindrome(input):
    str = ''
    for s in input:
        if(s.isalpha()):
            str += s
    str = str.lower()

    length = len(str)
    for i in range(0, length):
        if(str[i] != str[length - 1 - i]):
            return False

    return True


print(palindrome('lol'))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I'am Adam."))

print(my_palindrome('lol'))
print(my_palindrome("Madam, I'm Adam."))
print(my_palindrome("Madam, I'am Adam."))
