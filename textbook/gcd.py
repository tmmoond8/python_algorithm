def gcd(a, b):
    if(a < b):
        big = b
        small = a
    else:
        big = a
        small = b
    if(small == 0):
        return big
    return gcd(small, big % small)

print(gcd(192, 72))
print(gcd(60, 48))
