class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r = 0,len(nums) - 1
        res = nums[0]
        #[3,4,5,6,1,2]
        #if sorted min would be on the right if not 1 will be present on the left
        while l <= r:
            if nums[l] < nums [r]:
                res = min(res,nums[l])
                break
            mid = (l + r) // 2
            res = min(res,nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return res


        