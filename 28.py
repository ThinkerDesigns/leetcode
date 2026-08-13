#Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = 0
        while not haystack.startswith(needle):
            if len(needle) <= len(haystack):
                idx += 1
                haystack = haystack[1:]
                print(idx,haystack)
            else:
                return -1
        return idx
