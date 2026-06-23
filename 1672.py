# Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for x in range(len(accounts)):
            test = 0
            for j in range(len(accounts[x])):
                test = test + accounts[x][j]
            if test > richest:
                richest = test
        return richest
