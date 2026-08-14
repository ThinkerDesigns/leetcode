# Number of Changing Keys
class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        changes = 0
        for x in range(len(s) - 1):
            if s[x] != s[x+1]:
                changes += 1
        return changes
