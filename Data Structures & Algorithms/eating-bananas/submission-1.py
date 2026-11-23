class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
                # adds all the piles using the first k sed
            
            if hours <= h:
                res = min(res, k)
                #only saves the min and thats why res lives inside the first if loop 
                r = k -1
            else:
                l = k + 1
                

        return res