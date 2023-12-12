grid = [[3,2,1],[1,7,6],[2,7,7]]

count = 0
columns = {}

for i in range(len(grid)):
    print ("new")
    total = 0
    for j in range(len(grid)):
        print (grid[i][j])
        total += grid[i][j]
    if total in columns:
        columns[total] += 1
    else:
        columns[total] = 1
    print (total)

print ("Columns")
print (columns)

for i in range(len(grid)):
    print ("New")
    total = 0
    for j in range(len(grid)):
        print (grid[j][i])
        total += grid[j][i]
    if total in columns:
        count += columns[total]
    print (total)

print (count)