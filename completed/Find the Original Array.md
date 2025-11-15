---
tags:
  - nvidia
  - medium
  - bitwise
link: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/?envType=company&envId=nvidia&favoriteSlug=nvidia-thirty-days
last_attempt: 2025-11-15
rate:
  - ★★★★
---
#### Variants


#### Problem
You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

`pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].`
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.

 

Example 1:

>Input: pref = [5,2,0,3,1]
Output: [5,7,2,3,2]
Explanation: From the array [5,7,2,3,2] we have the following:
>- pref[0] = 5.
>- pref[1] = 5 ^ 7 = 2.
>- pref[2] = 5 ^ 7 ^ 2 = 0.
>- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
>- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

#### Notes
What's important is the property that `n ^ n = 0`. 

Each value in the `pref` array is a prefix of the XOR up to `i` (inclusive).

Another way to think about it is:

>`pref[i] = arr[0] ^ arr[1] ^ .. ^ arr[i]`

With that in mind, we can say that:

```
pref[1] ^ pref[0] = 
(arr[0] ^ arr[1]) ^ arr[0] = 
```

Which simplifies to `arr[1]` because `arr[0]`'s cancel out

So in essence, we `arr[i] = pref[i] ^ pref[i-1]` because we negating **all of the repeating terms** because `pref[i-1` will have everything that `pref[i]` has except for the newest ter,.


#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(1)

```go
func findArray(pref []int) []int {
    res := make([]int, len(pref))
    res[0] = pref[0]
    for i := 1; i < len(pref); i++ {
        res[i] = pref[i] ^ pref[i-1]
    }
    return res
}
```
