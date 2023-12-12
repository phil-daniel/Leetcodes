isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]

visited = set()

count = 0
while len(visited) < len(isConnected):
    for i in range(len(isConnected)):
        if not (i in visited):
            print ("Not visited", i)
            count += 1
            queue = [i]
            while len(queue) > 0:
                new = queue.pop(0)
                print ("visiting", new)
                visited.add(new)
                for j in range(len(isConnected)):
                    if isConnected[new][j] == 1:
                        if not (j in visited):
                            print ("adding to queue", j)
                            queue.append(j)

print (count)