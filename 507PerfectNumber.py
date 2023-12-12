num = 28

calc = 0
start = num // 2
while start > 0:
    print ("Looping", start)
    print ("Current total", calc)
    if num % start == 0:
        print ("Num True")
        calc += start
        if calc > num:
            print (False)
            exit()
    start -= 1
print (calc == num)