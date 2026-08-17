# Strictly Palindromic Number
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n):
            tmp = ""
            x = n
            while x >= 1:
                tmp += str(x % i)
                x = x // 2
            left = 0
            right = len(tmp) - 1
            while left <= right:
                if tmp[left] != tmp[right]:
                    return False
                left += 1
                right -= 1
        return True
