
def recursive_max(a, num):
    if(len(a) == 0):
        return num
    return recursive_max(a[1:len(a)], max(num, a[0]))

print(recursive_max([1, 5, 6, 9, 2, 8, 3], 0))
