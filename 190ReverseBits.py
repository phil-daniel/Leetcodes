n = bin(00000010100101000001111010011100)

newNum = 0
while n > 0:
    print (n - ((n >> 1) << 1))
    newNum = (newNum << 1) + n - ((n >> 1) << 1)
    n = n >> 1
print (newNum)