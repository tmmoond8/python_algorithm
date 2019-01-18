def fivo(n):
    if(n < 3):
        return 1
    return fivo(n - 1) + fivo(n - 2)

print(fivo(3))
print(fivo(18))