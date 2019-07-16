def students2(a):
    d = dict()
    for v in a:
        keyValue = v.split(":")
        d[int(keyValue[0].strip())] = keyValue[1].strip()

    def getStudent(num):
        if (num in d):
            return d[num]
        return "?"

    return getStudent


input = ["39: Justin", "14: John", "67: Mike", "105: Summer"]

getStudent = students2(input)
print(getStudent(39))
print(getStudent(14))
print(getStudent(67))
print(getStudent(22))
