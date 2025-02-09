```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seq = set(nums)
        cnt = 0
        for n in nums: 
            tmp_cnt = 0
            # If a larger number in the sequence exists
            # just skip this one.
            if n+1 in seq: continue
            cur = n
            # Loop downwards until all the values are captured
            while cur in seq:
                cur =- 1
                tmp_cnt += 1
            cnt = max(cnt, tmp_cnt)

        return cnt

s = Solution()
print(s.longestConsecutive([2,20,4,10,3,4,5]))
```
