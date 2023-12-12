matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 10

row = 0
while row < len(matrix)-1 and matrix[row+1][0] <= target:
    row += 1
print (row)