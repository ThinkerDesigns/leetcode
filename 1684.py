# Count the Number of Consistent Strings
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = len(words)
        for x in words:
            for i in x:
                if i not in allowed:
                    result -= 1
                    break
        return result
