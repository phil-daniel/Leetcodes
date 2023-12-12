rooms = [[1,2],[2,1],[1]]

visited = [-1] * len(rooms)
queue = rooms[0]
visited[0] = 1
count = 1

while len(queue) > 0:
    nextVisit = queue.pop()
    visited[nextVisit] = 1
    count += 1
    for i in rooms[nextVisit]:
        if visited[i] == -1:
            queue.append(i)

print (visited)
print (count == len(rooms))