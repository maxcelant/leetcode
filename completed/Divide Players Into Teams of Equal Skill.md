---
tags:
  - medium
  - hashing
  - jpmorgan
link: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/?envType=company&envId=jpmorgan&favoriteSlug=jpmorgan-thirty-days
last_attempt: 2025-10-26
rate:
  - ★★★★
---
#### Variants


#### Problem
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

 

Example 1:

>Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

#### Notes
Similar to [[Two Sum]] in a way, except you need to calculate the target.

The target is basically the `(sum(arr) * 2) / n`. The reason is because the target is the average of every 2 players, not 1 player.

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        freq = Counter(skill)
        n = len(skill)

        # The target value for each pair is the 
        # total sum of the list divided by n / 2
        # bc we want it counts for 2 players, not just one
        target = sum(skill) // (n // 2)
        res = 0
        for player in skill:
            # This value is already accounted for
            if freq[player] == 0:
                continue
            
            diff = target - player
            if diff not in freq or freq[diff] == 0:
                return -1
            freq[player] -= 1
            freq[diff] -= 1
            res += player * diff
        return res
            
# 36 // 6 = 
```


#### Follow Up: *""*

```python

```