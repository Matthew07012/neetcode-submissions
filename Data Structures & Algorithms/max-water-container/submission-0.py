class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = []
        i,j = 0, len(heights) - 1

        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            res.append(area)
            if heights[i] < heights[j]:
                i += 1
            else: 
                j -= 1
        
        return max(res)