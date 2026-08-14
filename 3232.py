# Find if Digit Game Can Be Won
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for x in nums:
            if x > 9:
                double += x
            else:
                single += x
        if single == double:
            return False
        return True
