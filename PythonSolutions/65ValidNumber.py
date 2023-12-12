def isInt(s: str) -> bool:
    sign = False
    for i in s:
        if i == '+' or i == '-':
            if sign:
                return False
            sign = True
        elif ord(i) < 48 or ord(i) > 57:
            return False
    if len(s) == 0 or (len(s) <= 1 and sign):
        return False
    if sign and (s[0] != '+' or s[0] == '-'):
        return False
    return True

def isDecimal(s: str) -> bool:
    sign = False
    dot = False
    for i in s:
        if i == '+' or i == '-':
            if sign:
                print ("Extra sign")
                return False
            sign = True
        elif i == '.':
            if dot:
                print ('extra dots')
                return False
            dot = True
        elif ord(i) < 48 or ord(i) > 57:
            print ("bad character")
            return False
    if (not dot) or (len(s) == 1 and dot) or (sign and dot and len(s)==2):
        print ("no numbers")
        return False
    if sign and (s[0] != '+' or s[0] != '-'):
        print ("sign in wrong place")
        return False
    return True

 # Goes either decimal, integer, decimal E integer, decimal

s = "-1."

decimal = False
exponent = -1

for i in range(len(s)):
    if s[i] == 'E' or s[i] == 'e':
        exponent = i
    if s[i] == '.':
        decimal = True

if (exponent != -1) and decimal:
     print ("exponent and decimal")
     print (isDecimal(s[:exponent]) and isInt(s[exponent+1:]))
elif (exponent != -1) and not decimal:
     print ("exponent and ints")
     print (isInt(s[:exponent]) and isInt(s[exponent+1:]))
elif decimal:
     print ("decimal")
     print (isDecimal(s))
else:
     print ("int")
     print (isInt(s))