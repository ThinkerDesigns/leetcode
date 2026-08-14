# Difference Between Element Sum and Digit Sum of an Array
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        eSum = 0
        dSum = 0
        digits = ""
        for x in nums:
            eSum += x
        for x in nums:
            if x > 9:
                digits += str(x)
            else:
                dSum += x
        digits = list(digits)
        for x in digits:
            dSum += int(x)
        return abs(eSum - dSum)
