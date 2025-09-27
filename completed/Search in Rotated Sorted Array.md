---
tags:
  - binary-search
  - medium
rating: 3
last_attempt: 2025-05-10
pattern: Determine which side you are on, then figure out how to shrink depending on where the target is.
---
#### Intuition
---
- Use binary search, duh.

#### Code
---

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            # Check if in the left section
            if nums[l] <= nums[mid]:
                # If the target is greater than the middle
                if target > nums[mid]:
                    l = mid + 1
                # If the target is less than the left pointer
                elif target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                
            # Check if in the right section
            else:
                # If the target is less than the middle
                if target < nums[mid]:
                    r = mid - 1
                # If the target is greater than the right
                elif target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1 
        return -1
```

#### Insight
---
- With problems like this, you need to split it up into cases.
- The important distinction is the position of the `middle` index—and whether it's in the left or right section.
- If we are in the left section, we want to think of the possible cases in which the target is _somewhere_ on the right side. There are too main cases. Either it's bigger than `middle` or it's less than `left`.
- Same goes with right section. It's either less than `middle` or greater than `right`. 

>![[Pasted image 20250306201940.png]]

>![[Pasted image 20250306202203.png]]

#### Takeaways
---
- **Where did I go wrong?**
	- This one was conceptually difficult for me to differentiate the cases.
- **Lessons Learned?**
	- I should try my best to split this problem into understandable cases, aka the left and right partitions.
- **Aha Moments?**
	- Using the pictures to glue it in my head helped a lot.