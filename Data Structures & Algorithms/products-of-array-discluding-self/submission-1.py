class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            products = 1
            for j in range(len(nums)):
                if i != j:
                    products *= nums[j]

            answer.append(products)

        return answer