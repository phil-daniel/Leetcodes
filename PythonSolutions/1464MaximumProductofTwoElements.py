def maxProduct(self, nums: [int]) -> int:
    nums.sort()
    return (nums[-1] - 1) * (nums[-2] - 1) 
maxProduct([0,1,2,3,4,5])