# Find Words Containing Character
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            test = list(words[i])
            if x in test:
                result.append(i)
        return result
