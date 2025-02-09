
'''
You are given an array of integers nums and an integer k. 
Find the length of the longest contiguous subarray whose sum is less than or equal to k. Return 0 if no such subarray exists.
'''


class Solution:
    def longestSubarrayNaive(self, nums: list[int], k: int) -> int:
        total = 0
        window = []
        for r in range(len(nums)):
            window.append(nums[r])
            while sum(window) > k:
                window.pop(0)
            total = max(total, len(window))
        return total

    def longestSubarrayOptimized(self, nums: list[int], k: int) -> int:
        l = 0
        window = 0
        total = 0
        for r in range(len(nums)):
            window += nums[r]
            while window > k:
                window -= nums[l]
                l += 1
            total = max(total, (r - l) + 1)
        return total




s = Solution()
tests = [
    ([1,2,3,4,5], 9, 3),
    ([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 8, 3),
    ([5, 6, 7, 8, 9], 4, 0)
]
for t in tests:
    nums, k, expect = t
    actual = s.longestSubarrayNaive(nums, k)
    assert expect == actual, "Incorrect!"

