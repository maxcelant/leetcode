---
tags:
  - strings
  - easy
  - meta
link: https://leetcode.com/problems/longest-common-prefix
last_attempt: 2025-11-06
rate:
  - ★★★★
---
#### Variants


#### Problem
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

>**Input:** strs = ["flower","flow","flight"]
**Output:** "fl"

**Example 2:**

>**Input:** strs = ["dog","racecar","car"]
**Output:** ""
**Explanation:** There is no common prefix among the input strings.

#### Notes
We start by ass

#### Code
**Time Complexity**:
**Space Complexity**: 

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            while len(prefix) > 0 and s[:len(prefix)] != prefix:
                prefix = prefix[:-1]
            if prefix == "":
                return ""
        return prefix

```
