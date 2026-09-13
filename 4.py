# Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp = sorted(nums1 + nums2)
        left = 0
        right = len(tmp) - 1       
        while left <= right:
            left += 1
            right -= 1
        if len(tmp) % 2 == 1:
            return tmp[left - 1]
        return (tmp[left] + tmp[right]) / 2
