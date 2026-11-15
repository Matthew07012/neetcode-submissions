class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #its list of list
        #len matrix returns number of list

        rows, cols = len(matrix), len(matrix[0])
        l,r = 0, rows * cols - 1

        while l <= r:
            mid = (l+r)//2
            val = matrix [mid//cols][mid % cols]
            if val == target:
                return True
            elif val < target:
                l += 1
            else:
                r -= 1
        return False