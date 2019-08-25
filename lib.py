
# 'abcd' => ['a', 'b', 'c', 'd']
def string2list(string): 
    return list(str(string))


# [1, 2, 3] => [1, 2, 3], [2, 3, 1], [3, 1, 2]
def curcuitArray(arr):
    N = len(arr)
    for i in range(0, N):
        print(arr[i: N] + arr[0: i])

# ord('a') => 97, chr(97) => 'a'
def curcuitAlpha():
    for code in range(ord('a'), ord('z') + 1):
        print(chr(code))