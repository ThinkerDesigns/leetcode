# Digit Frequency Score
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        tmp = list(str(n))
        freq = {}
        result = 0
        for x in tmp:
            freq[x] = freq.get(x,0) + 1
        for x in freq:
            result = result + (int(x) * freq[x])
        return result
