def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber


abcd = modASCII("ABCD", 24)
efgh = modASCII("EFGH", 24)
rstu = modASCII("RSTU", 24)

print("hashed value: ", abcd)
print("hashed value: ", efgh)
print("hashed value: ", rstu)
