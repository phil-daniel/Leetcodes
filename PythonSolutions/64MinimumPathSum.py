grid = [[1,3,1],[1,5,1],[4,2,1]]

rows, columns = len(grid), len(grid[0])


for i in range(2, rows+1):
    grid[rows-i][columns-1] += grid[rows-i+1][columns-1]

for i in range(2, columns+1):
    grid[rows-1][columns-i] += grid[rows-1][columns-i+1]
for x in range(2, columns+1):
    for y in range(2, rows+1):
        grid[rows-y][columns-x] += min(grid[rows-y+1][columns-x], grid[rows-y][columns-x+1])
print (grid)