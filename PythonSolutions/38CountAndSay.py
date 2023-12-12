n = 4

count = 1
ans = "1"

while count < n:
    newAns = ""

    i = 1
    pos = 1
    while pos < len(ans):
        if ans[pos-1] == ans[pos]:
            i += 1
        else:
            print ("Test")
            newAns = newAns + str(i) + ans[pos-1]
            i = 1
        pos += 1
    newAns = newAns + str(i) + ans[-1]
    ans = newAns
    count += 1
        
print (ans)
        