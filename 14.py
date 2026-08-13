#Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = max(strs)
        for x in strs:
            while not x.startswith(prefix):
                print(prefix)
                prefix = prefix[:-1]
        return prefix
