# Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num
        middle = (start+end) // 2
        while start <= end:
            if (middle * middle) == num:
                return True
            elif (middle * middle) <= num:
                start = middle + 1
                middle = (start+end) // 2
            elif (middle * middle) >= num:
                end = middle - 1
                middle = (start+end) // 2
        return False
