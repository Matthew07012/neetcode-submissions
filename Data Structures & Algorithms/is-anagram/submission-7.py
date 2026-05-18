class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
        
#sort string first then test  
s = "racecar" 
t = "carrace"

sol = Solution()

print(sol.isAnagram(s,t))