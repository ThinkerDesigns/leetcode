# Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(str(n))
        prodDig = 1
        sumDig = 0
        for x in n:
            prodDig = prodDig * int(x)
            sumDig += int(x)
        return (prodDig - sumDig)
