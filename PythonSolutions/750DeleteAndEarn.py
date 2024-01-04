def deleteAndEarn(nums) -> int:
        count = {}
        for i in nums:
            if count.get(i):
                count[i] += 1
            else:
                count[i] = 1
        dp = [0] * (max(nums)+1)
        if count.get(1):
            dp[1] = count[1]
        for i in range(2, len(dp)):
            holder = dp[i-2]
            if count.get(i):
                holder += (count[i] * i)
            dp[i] = max(dp[i-1], holder)
        return dp[-1]

print (deleteAndEarn([3,4,2]))