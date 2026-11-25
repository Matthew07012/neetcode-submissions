class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums) - 1
        res = -1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                res = mid
                break

            if nums[l] <= nums[mid]:  #if left side is sorted
                if nums[l] <= target < nums[mid]:  #if target in range
                    r = mid - 1 #discard right half
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return res
