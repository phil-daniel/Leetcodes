s = "bbcbaba"
substr = set()
front = 0
back = len(s)-1

while front + 1 < back:
    print (front, back)
    if s[front] == s[back]:
        for i in range(front+1, back):
            substr.add(s[front] + s[i] + s[back])
        front += 1
        back -= 1
    elif s[front] == s[back-1]:
        back -= 1
    elif s[front+1] == s[back]:
        front += 1
    else:
        front += 1
        back -= 1
print (list(substr))
        