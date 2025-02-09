from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # If the total is less than the target, increase left pointer
        # If the total is greater than the target, decrease rught pointer
        l, r = 0, len(numbers) - 1
        while l < r:
            cur = numbers[l] + numbers[r]
            if cur == target: return [l + 1, r + 1]
            if cur > target: r -= 1
            if cur < target: l += 1
            
        return [-1,-1]

s = Solution()
print(s.twoSum([1,2,3,4], 3))
