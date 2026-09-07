# Convert Date to Binary
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        tmp = date.split("-")
        for x in range(len(tmp)):
            tmp[x] = format(int(tmp[x]), "b")
        tmp = "-".join(tmp)
        return tmp
