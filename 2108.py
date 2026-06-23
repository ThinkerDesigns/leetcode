# Find First Palindromic String in the Array
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for x in range(len(words)):
            if words[x] == words[x][::-1]:
                return words[x]
        return ""
