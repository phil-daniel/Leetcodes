def findDiagonalOrder(nums: []) -> []:
    ans = []
    for i in range(len(nums)):
        for j in range(i, -1, -1):
            if len(nums[j]) >= j and len(nums) >= j:
                ans.append(nums[j][i-j])
    return ans

print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))