# Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        tmp = list(str(x))
        left = 0
        right = len(tmp) - 1
        if tmp[left].isalnum() == False:
            left += 1
        while left <= right:
            temp = tmp[left]
            tmp[left] = tmp[right]
            tmp[right] = temp
            left += 1
            right -= 1
        tmp = "".join(tmp)
        if -2147483648 <= int(tmp) <= 2147483647:
            return int(tmp)
        return 0
