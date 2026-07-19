# Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) 
        middle =  (start + end) // 2
        while start <= end:
            if start in nums:
                start = start + 1
            else:
                return start
