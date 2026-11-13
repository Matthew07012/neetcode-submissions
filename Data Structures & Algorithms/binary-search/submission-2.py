class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums) - 1

        while l <= r and target in nums:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid -1
                while target == nums[r]:
                    return r
            else:
                l = mid + 1
                while target == nums[l]:
                    return l
        return -1
        