
from collections import defaultdict
import heapq
from typing import List


class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq = defaultdict(int) 
    for n in nums:
      freq[n] += 1
    
    heap = []
    for n in freq.keys():
      heapq.heappush(heap, (freq[n], n))
      if len(heap) > k:
        heapq.heappop(heap)

    print(heap)
    
nums = [1,2,2,3,3,3]
k = 2
s = Solution()
s.topKFrequent(nums, k)