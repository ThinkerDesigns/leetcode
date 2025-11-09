/*Plus One*/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ''.join(map(str, digits))
        x = int(x)
        x = x + 1
        digits = res = [int(i) for i in str(x)]
        return digits
