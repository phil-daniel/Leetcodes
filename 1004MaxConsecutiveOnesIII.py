nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

flipped = []
front = 0
back = 0

curr = 0
maxi = 0

print (nums)

while back < len(nums):
    if nums[back] == 1:
        curr += 1
    else:
        if len(flipped) > k-1:
            pos = flipped.pop(0)
            if pos > front:
                front = pos
                curr = back - front - 1
        flipped.append(back)
        curr += 1
    back += 1
    maxi = max(maxi, curr)
    print ("New")
    print ("Curr: " + str(curr))
    print ("Maxi: " + str(maxi))
    print ("Flipped: " + str(flipped))

print (maxi)