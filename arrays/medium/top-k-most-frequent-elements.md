
from collections import defaultdict
import heapq
from typing import List


class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Determine frequency of each number
    freq = defaultdict(int) 
    for n in nums:
      freq[n] += 1
    
    heap = [] # Heaps are min-heap by default
    for n in freq.keys():
      heapq.heappush(heap, (freq[n], n))
      if len(heap) > k:
        heapq.heappop(heap) # Popping the top of the heap (smallest)

    return [n for (_, n) in heap]


nums = [1,2,2,3,3,3]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))