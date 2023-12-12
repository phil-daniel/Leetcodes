nums = [1,1,0,1,1,1]

back = 0

curr = 0
maxi = 0

while back < len(nums):
    if nums[back] == 1:
        curr += 1
    else:
        curr = 0
    back += 1
    maxi = max(maxi, curr)
    print (curr)
    print ("maxi: " + str(maxi))
print (maxi)