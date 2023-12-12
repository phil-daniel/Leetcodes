setArray = [{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
            {'a', 's', 'd', 'f', 'g', 'h', 'j' ,'k', 'l'},
            {'z', 'x', 'c', 'v', 'b', 'n', 'm'}]
        
words = ["Hello","Alaska","Dad","Peace"]


answer = []
for word in words:
    inSet = 0
    for sets in range(len(setArray)):
        print (word[0])
        if word[0].lower() in setArray[sets]:
            print ("found in set")
            inSet = sets
            break
    print ("inSet" + str(inSet))
    isIn = True
    for letter in word:
        if letter.lower() not in setArray[sets]:
            isIn = False
            break
    if isIn:
        answer.append(word)

print (answer)