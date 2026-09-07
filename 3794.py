# Reverse String Prefix
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if k == 1:
            return s
        if k == len(s):
            return s[::-1]
        tmp = list(s[:k])
        s = s[k:]
        left = 0
        right = len(tmp) - 1
        while left <= right:
            temp = tmp[left]
            tmp[left] = tmp[right]
            tmp[right] = temp
            left += 1
            right -= 1
        tmp = "".join(tmp)
        return tmp + s
