senate = "RDD"
while True:
    print ("New loop")
    newVoters = ""
    pos = 0
    skips = 0
    while pos < len(senate):
        newVoters += senate[pos]
        if pos == len(senate)-1 and senate[-1] != senate[0]:
            newVoters = newVoters[1:]
            pos += 2
        elif senate[(pos+1) % len(senate)] != senate[pos]:
            pos += 2
            skips += 1
        else:
            pos += 1
    senate = newVoters
    print (senate)
    if skips == 0:
        print (senate[0])
        exit()