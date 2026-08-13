# Check if the Sentence Is Pangram
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq = {}
        for x in sentence:
            freq[x] = freq.get(x,0) + 1
        if len(freq) == 26:
            return True
        return False
