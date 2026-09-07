# Find Most Frequent Vowel and Consonant
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        freq = {}
        maxV = 0
        maxC = 0
        for x in s:
            freq[x] = freq.get(x,0) + 1
        for x in freq:
            if x in vowels and freq[x] > maxV:
                maxV = freq[x]
            elif x not in vowels and freq[x] > maxC:
                maxC = freq[x]
        return maxC + maxV
