# Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for x in nums:
            result.append(x * x)
        return sorted(result)
