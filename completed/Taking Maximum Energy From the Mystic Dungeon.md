---
tags:
  - medium
  - jpmorgan
  - two-pointers
  - amazon
link: https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/?envType=company&envId=jpmorgan&favoriteSlug=jpmorgan-thirty-days
last_attempt: 2025-10-27
rate:
  - ★★★★
---
#### Variants


#### Problem
In a mystic dungeon, `n` magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

You have been cursed in such a way that after absorbing energy from magician `i`, you will be instantly transported to magician `(i + k)`. This process will be repeated until you reach the magician where `(i + k)` does not exist.

In other words, you will choose a starting point and then teleport with `k` jumps until you reach the end of the magicians' sequence, **absorbing all the energy** during the journey.

You are given an array `energy` and an integer `k`. Return the **maximum** possible energy you can gain.

**Note** that when you are reach a magician, you _must_ take energy from them, whether it is negative or positive energy.

**Example 1:**

**Input:** energy = [5,2,-10,-5,1], k = 3

**Output:** 3

**Explanation:** We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

#### Notes
We start from all possible endings from `n-k` to `k`. For each of those, we shift backwards by `k` and accumulate the total for that chain.

The max we find is the answer!

![[Pasted image 20251027140850.png]]

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```python
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        res = float('-inf')
        # Try all possible chain ends
        for i in range(n - k, n):
            # cur = energy[i]
            cur = 0
            j = i
            # Try this entire chain to see if it's max is higher
            while j >= 0:
                cur += energy[j]
                res = max(res, cur)
                j -= k
        return res
```


#### Follow Up: *""*

```python

```