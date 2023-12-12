nums = [1,2,3,4,5,6]
k = 2

for i in range(k):
    print ("New LOOOOOOP")
    holder = nums[-1]
    print ("Before")
    print (nums)
    for i in range(len(nums)):
        newHolder = nums[i]
        nums[i] = holder
        holder = newHolder


    print ("after")
    print (nums)