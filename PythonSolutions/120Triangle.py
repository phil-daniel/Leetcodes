triangle = [[-1],[2,3],[1,-1,-3]]

if len(triangle) == 1:
    print (triangle[0][0])
    exit()

for i in range(1, len(triangle)):
    triangle[i][0] += triangle[i-1][0]
    triangle[i][-1] += triangle[i-1][-1]
        
for i in range(2, len(triangle)):
     for j in range(1, len(triangle[i])-1):
        triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        
print(triangle)