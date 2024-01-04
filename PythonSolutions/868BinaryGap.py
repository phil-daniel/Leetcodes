def binaryGap(n : int) -> int:
    maxi, curr, can = 0, 1, False
    while n > 0:
        if (n >> 1) != (n / 2):
            print ("One")
            if not can:
                can = True
                curr = 1
            else:
                maxi = max(maxi, curr)
                curr = 1
        else:
            print ("Not")
            curr += 1
        n = n >> 1
    return maxi

print (binaryGap(6))