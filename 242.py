# Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}
        if len(s) != len(t):
            return False
        for x in s:
            freqS[x] = freqS.get(x,0) + 1
        for x in t:
            freqT[x] = freqT.get(x,0) + 1
        for i in freqS:
            if (i not in freqT) or (freqS[i] != freqT[i]):
                return False
        return True
        
