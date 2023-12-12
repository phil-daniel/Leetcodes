nums = [1,2,3,1]

if len(nums) == 1 or nums[0] > nums[1]:
    print (0)
    exit()
elif nums[-1] > nums[-2]:
    print (len(nums)-1)
    exit()
    
front = 0
back = len(nums)-1
middle = 0

while front < back-1:
    middle = (back-front) // 2 + front
    if nums[middle-1] < nums[middle] and nums[middle] > nums[middle+1]:
        print ("found here")
        print (middle)
        exit()
    elif nums[middle-1] < middle:
        front = middle
    else:
        back = middle

print ("Not found until here")
print (middle)