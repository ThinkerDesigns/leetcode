# Single Number II 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0) + 1
        for x in freq:
            if freq[x] == 1:
                return x
