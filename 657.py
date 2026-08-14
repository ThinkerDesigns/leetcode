# Robot Return to Origin
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = {'R': 0, 'L': 0, 'U': 0, 'D': 0}
        for x in moves:
            pos[x] = pos.get(x,0) + 1
        print(pos)
        if (pos["L"] != pos["R"]) or (pos["U"] != pos["D"]):
            return False
        return True
