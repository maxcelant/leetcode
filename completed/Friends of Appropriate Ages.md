---
tags:
  - medium
  - meta
  - strings
link: https://leetcode.com/problems/friends-of-appropriate-ages/
last_attempt: 2025-11-12
rate:
  - ★★★
---
#### Problem
There are `n` persons on a social media website. You are given an integer array `ages` where `ages[i]` is the age of the `ith` person.

A Person `x` will not send a friend request to a person `y` (`x != y`) if any of the following conditions is true:

- `age[y] <= 0.5 * age[x] + 7`
- `age[y] > age[x]`
- `age[y] > 100 && age[x] < 100`

Otherwise, `x` will send a friend request to `y`.

Note that if `x` sends a request to `y`, `y` will not necessarily send a request to `x`. Also, a person will not send a friend request to themself.

Return _the total number of friend requests made_.

**Example 1:**

**Input:** `ages = [16,16]`
**Output:** 2
**Explanation:** 2 people friend request each other.

**Example 2:**

**Input:** `ages = [16,17,18]`
**Output:** 2
**Explanation:** Friend requests are made 17 -> 16, 18 -> 17.

#### Notes
We want to check every age against every age (including the same age).

Instead of iterating through each person, we count the number of people at a given age. If the conditions are not met (pass), then we multiply the counts of people in both ages. Each person in one age will send a friend request to _everyone in the other group_.

The only caveat is when we are looking at the same age group.

**Example**:
Let's say we have three 16 year olds. Each person will send a friend request to every other person. But not themselves! duh! 

person 1: 2 friend requests
person 2: 2 friend requests
person 3: 2 friend requests

So that would be `N * (N - 1)` total friend requests.

#### Code
**Time Complexity**: O(N^2)
**Space Complexity**: O(1)

```python
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_count = [0] * 121
        for age in ages:
            age_count[age] += 1
        res = 0
        for ageA, countA in enumerate(age_count):
            for ageB, countB in enumerate(age_count):
                # No friend request conditions
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                # If the people are same age, they can't
                # friend request themselves.
                if ageA == ageB:
                    res += countA * (countA - 1)
                else:
                    res += countA * countB
        return res

```
