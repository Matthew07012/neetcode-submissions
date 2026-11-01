class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0 , len(numbers) - 1

        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i + 1,j + 1]
            elif total < target: #needs bigger sum because it is an ascending order so loops up vice versa
                i += 1
            else:
                j -= 1