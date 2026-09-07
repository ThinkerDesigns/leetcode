# Mirror Distance of an Integer
class Solution:
    def mirrorDistance(self, n: int) -> int:
        tmp = [int(x) for x in str(n)]
        left = 0
        right = len(tmp) - 1
        while left <= right:
            temp = tmp[left]
            tmp[left] = tmp[right]
            tmp[right] = temp
            left += 1
            right -= 1
        print(tmp)
        tmp = int("".join(map(str, tmp)))
        return abs(int(tmp) - n)
