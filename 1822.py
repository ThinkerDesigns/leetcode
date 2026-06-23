# Sign of the Product of an Array
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        test = 1
        if 0 in nums:
            return 0
        else:
            for x in range(len(nums)):
                test = test * nums[x]
            if test > 0:
                return 1
            elif test < 0:
                return -1
