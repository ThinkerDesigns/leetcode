# Find Closest Person
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        tmp = abs(z-x)
        tmp2 = abs(z-y)
        if tmp > tmp2:
            return 2
        if tmp2 > tmp:
            return 1
        return 0
