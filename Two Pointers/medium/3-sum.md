```python
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            # If the current number is greater than 0, we can't find a triplet summing to 0
            if nums[i] > 0: 
                break
            # Skip duplicate numbers to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]: 
                continue  
            l, r = i + 1, len(nums) - 1
            while l < r:
                target = nums[l] + nums[r] + nums[i]
                if target == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates for l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Skip duplicates for r
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif target < 0:
                    l += 1
                else:
                    r -= 1
        return res

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
```