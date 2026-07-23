# Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        while left <= len(nums) - 1:
            for x in range(len(nums) - 1):
                if ((nums[left] + nums[x]) == target) and (left != x):
                    return [left,x]
            left +=1
