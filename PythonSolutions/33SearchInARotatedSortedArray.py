nums = [1,3,5]
target = 2

front = 0
back = len(nums) - 1
if nums[0] == target:
    print (0)
    exit()
elif nums[back] == target:
    print (back)
    exit()
while front < back:
    middle = (front + back) // 2
    print (front, middle, back)
    if nums[middle] == target:
        print (middle)
        exit()
    elif nums[middle] > nums[back] and target < nums[back]:
        front = middle
    elif nums[middle] < nums[front] and target > nums[front]:
        back = middle
    elif nums[middle] > target:
        back = middle
    else:
        front = middle
print (-1)