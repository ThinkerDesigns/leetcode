# Count Digit Appearances
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for x in nums:
            for k in str(x):
                if k == str(digit):
                    count += 1
        return count
