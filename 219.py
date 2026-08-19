# Contains Duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tmp = {}
        for i in range(len(nums)):
            if nums[i] in tmp:
                if i - tmp[nums[i]] <= k:
                    return True
            tmp[nums[i]] = i
        return False
