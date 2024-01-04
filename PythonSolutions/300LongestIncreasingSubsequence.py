def lengthOfLIS(nums) -> int:
    ans = [1] * len(nums)
    for i in range(len(ans)-2, -1, -1):
        pos, maxi = i + 1, 0
        while pos < len(nums):
            if nums[i] < nums[pos]:
                maxi = max(maxi, ans[pos])
            pos += 1
        ans[i] = 1 + maxi
    print (ans)
    return max(ans)
        

print (lengthOfLIS([0,1,0,3,2,3]))