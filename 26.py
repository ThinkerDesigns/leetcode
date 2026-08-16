# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        i = 0
        tmp = len(nums)
        while i < tmp:
            if nums[i] not in result:
                result.append(nums[i])
            i += 1
        nums.extend(result)
        for i in range(tmp):
            del nums[0]
        return len(nums)
