# First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        idx = 0
        for x in s:
            freq[x] = freq.get(x,0) + 1
        print(freq)
        for x in freq:
            if (freq[x] == 1):
                idx = s.index(x)
                return idx
        return -1
