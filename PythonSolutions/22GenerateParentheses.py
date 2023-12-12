n=3

s = {"()"}
curr = 1
while curr < n:
    newS = set()
    for i in s:
        newS.add(i + "()")
        for j in range(len(i)):
            if i[j] == "(":
                print ("Tests")
                print (i)
                print (i[:j+1])
                print (i[j+1:])
                print ("new?")
                print (i[:j+1] + "()" + i[j+1:])
                newS.add(i[:j+1] + "()" + i[j+1:])
            print (newS)
        s = newS
    curr += 1
print (list(s))