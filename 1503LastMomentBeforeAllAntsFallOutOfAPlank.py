n = 4

left = [4,3]
right = [0,1]


turns = 0
while len(left) > 0 or len(right) > 0:
    print ("New Loop")
    print (left)
    print (right)
    newLeft = []
    newRight = []
    rightSet = set(right)
    leftSet = set(left)
    for i in left:
        if (i in rightSet):
            if (i+1) <= n:
                newRight.append(i+1)
        if (i-1 in rightSet):
            newRight.append(i)
        else:
            if i-1 <= 0:
                newLeft.append(i-1)
    for i in right:
        if (i in leftSet):
            if (i-1) >= 0:
                newLeft.append(i-1)
        if (i+1 in leftSet):
            newLeft.append(i)
        else:
            if i-1 <= n:
                newRight.append(i+1)
    left = newLeft
    right = newRight
    turns += 1
print (turns)