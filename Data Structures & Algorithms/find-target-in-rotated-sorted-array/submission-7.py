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
#     It's about the current search range l..r, not the size of the original array. Every binary search shrinks its range down to 1 or 2 elements at the end, no matter how big the array started.

# So with nums of 1,000,000 elements, after about 19 rounds the range l..r is small, and l == mid can happen then. If the target is still in there, the < bug bites at that point.

# You only notice it on short inputs like [1, 3] because with a short array the range is 1 or 2 elements from the very first iteration, and in a long array it only shows up on the last steps, and may or may not affect the answer depending on where the target is.

# So always use <=. It's the correct check for any size.