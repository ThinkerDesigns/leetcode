# Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        result = []
        for x in range(1,len(nums) + 1):
            result.append(sum(nums[:x]))
        return result
