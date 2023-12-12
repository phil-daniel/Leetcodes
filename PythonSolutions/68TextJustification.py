words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

answer = []
        
currLen = 0
new = []
        
pos = 0
while pos < len(words):
    if currLen + len(words[pos]) + 1 <= maxWidth:
        currLen += len(words[pos]) + 1
        new.append(words[pos])
        pos += 1
    else:
        spacesNeeded = maxWidth - currLen + len(new) - 1
        addTo = 0
        while spacesNeeded >= 0:
            if addTo >= len(new) - 1:
                addTo = 0
            print (new)
            print (addTo)
            new[addTo] = new[addTo] + ' '
            addTo += 1
            spacesNeeded -= 1
        answer.append("".join(new))
        currLen = 0
        new = []
answer.append("".join(new))
print (answer)