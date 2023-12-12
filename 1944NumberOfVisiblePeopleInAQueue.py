heights = [10,6,8,5,11,9]

ans = [0] * len(heights)
for i in range(len(heights)-1):
    currMax = 0
    pos = i+1
    count = 0
    while pos < len(heights) and currMax < heights[i]:
        if heights[pos] > currMax:
            print (i, "can see", pos)
            currMax = heights[pos]
            count += 1
        pos += 1
    ans[i] = count
print (ans)