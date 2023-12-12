nums = [1,12,-5,-6,50,3]
k = 4

front = -1
back = k-1
total = 0

for i in range(k):
    total += nums[i]
        
currMax = total
print (total)

while back < len(nums)-1:
    back += 1
    front += 1
    total = total - nums[front] + nums[back]
    print (total)
    currMax = max(total, currMax)

print (currMax/4)