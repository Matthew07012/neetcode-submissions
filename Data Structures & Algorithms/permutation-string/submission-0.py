class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count = {}
        res = False
        l = 0

        for r in range(len(s2)):
            if (r - l + 1) > len(s1):
                l += 1
            if sorted(s1) == sorted(s2[l : r + 1]):
                res = True
        return res