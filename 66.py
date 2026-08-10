# Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            return list(int(x) for x in str(digits[0] + 1))
        tmp = (int("".join(map(str, digits)))) + 1 # gpt :(
        return (list(int(x) for x in str(tmp)))
