nums = [2,1,1,2]

if len(nums) <= 2:
    print (max(nums))
    exit()
dp = [0] * len(nums)
dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]
for i in range(3, len(nums)):
    print (dp)
    dp[i] = nums[i] + max(dp[i-3], dp[i-2])
print(dp)