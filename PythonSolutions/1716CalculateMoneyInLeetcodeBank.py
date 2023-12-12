def totalMoney(n: int) -> int:
    total = 0
    lastMon = 0
    adding = 0
    while n > 0:
        lastMon += 1
        adding = lastMon
        total += adding
        print (adding)
        n -= 1
        for i in range(6):
            if n > 0:
                n-= 1
                adding += 1
                total += adding
                print (adding)
    return total

print (totalMoney(10))