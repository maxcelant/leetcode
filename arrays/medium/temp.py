from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * len(nums)
    pref = [1] * len(nums)
    post= [1] * len(nums)
    # Handle prefix
    for i in range(1, n):
      pref[i] = pref[i-1] * nums[i-1]
    for i in range(n - 2, -1, -1):
      post[i] = post[i+1] * nums[i+1]
    for i in range(n):
      res[i] = pref[i] * post[i]


    return res

nums = [1,2,4,6]
s = Solution()
print(s.productExceptSelf(nums))
