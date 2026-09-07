# Compute Alternating Sum
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        add = 0
        sub = 0
        i = 0
        while i < len(nums):
            if i % 2 == 0:
                add += nums[i]
            else:
                sub += nums[i]
            i += 1
        return add - sub
