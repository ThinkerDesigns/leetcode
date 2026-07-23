# Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = {}
        while left <= right:
            if nums[left] == nums[right]:
                if nums[left] not in result:
                    result[nums[left]] = 1
                else:
                    result[nums[left]] += 1
            left += 1
            right -= 1
        return max(result, key = result.get)
