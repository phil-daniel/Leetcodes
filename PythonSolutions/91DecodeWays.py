def numDecodings(s: str) -> int:
    if s[0] == '0':
        return 0
    ans, i = 1, len(s)-1
    while i >= 1:
        if s[i] == '0':
            i -= 2
        elif (49 <= ord(s[i]) <= 57 and s[i-1] == '1') or (49 <= ord(s[i]) <= 54 and s[i-1] == '2'):
            ans += 1
            print(i, s[i])
        i -= 1
        print(i, "looping")
    return ans

print ("ans ", str(numDecodings("1123")))