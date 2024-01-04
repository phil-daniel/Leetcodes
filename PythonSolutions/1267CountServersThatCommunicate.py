def countServers(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i > 0 and grid[i-1][j] == 1:
                        count += 1
                    elif j > 0 and grid[i][j-1] == 1:
                        count += 1
                    elif i < len(grid)-1 and grid[i+1][j] == 1:
                        count += 1
                    elif j < len(grid[0])-1 and grid[i][j+1] == 1:
                        count += 1

        return count
print(countServers([[1,0],[0,1]]))