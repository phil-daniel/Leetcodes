words = ["a","b","ba","bca","bda","bdca"]
print (words)

best = 1
curr = 1
for i in range(1, len(words)):
    if len(words[i-1]) + 1 != len(words[i]):
        best = max(best, curr)
        print ("Failed at", words[i])
        curr = 1
    else:
        fine = True
        w1, w2 = 0, 0
        while w1 < len(words[i-1]):
            if words[i-1][w1] != words[i][w2]:
                if w2 == w1 + 1:
                    fine = False
                    break
                else:
                    w2 += 1
            else:
                w1 += 1
                w2 += 1
        if fine:
            curr += 1
        else:
            print ("Failed at", words[i])
            best = max(best, curr)
            curr = 1
print (max(best, curr))

            