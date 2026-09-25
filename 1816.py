# Truncate Sentence
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        tmp = s.split(" ")
        tmp = tmp[:k]
        return " ".join(tmp)
