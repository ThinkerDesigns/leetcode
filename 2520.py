# Count the Digits That Divide a Number
class Solution:
    def countDigits(self, num: int) -> int:
        tmp = str(num)
        result = 0
        if len(tmp) == 1:
            return 1
        for x in tmp:
            if num % int(x) == 0:
                result += 1
        return result
