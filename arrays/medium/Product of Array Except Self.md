```python
from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    prefix = [0] * n
    suffix = [0] * n
    # Since there are no elements before index 0
    # And we "dont include the current element", then it needs to be just 1
    prefix[0] = 1
    # And no elements after n - 1, same thing as above
    suffix[n - 1] = 1
    # Find the product BEFORE the current element
    
    '''
    i	nums[i]	prefix[i] (product before i)
    0	  1	    1
    1	  2	    1
    2	  3	    1 x 2 = 2
    3	  4	    1 x 2 x 3 = 6
    '''
    for i in range(1, n):
      prefix[i] = nums[i - 1] * prefix[i - 1]
    print(prefix)
    for i in range(n - 2, -1, -1):
      suffix[i] = nums[i + 1] * suffix[i + 1]
    print(suffix)
    for i in range(n):
      res[i] = suffix[i] * prefix[i]
    return res


nums = [1,2,4,6]
s = Solution()
print(s.productExceptSelf(nums))
```