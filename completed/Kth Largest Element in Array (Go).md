---
tags:
  - nvidia
  - medium
  - heaps
link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-10-30
rate:
  - ★★★★
---
#### Variants


#### Problem
Given an integer array `nums` and an integer `k`, return _the_ `kth` _largest element in the array_.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?

**Example 1:**

**Input:** nums = [3,2,1,5,6,4], k = 2
**Output:** 5

**Example 2:**

**Input:** nums = [3,2,3,1,2,4,5,5,6], k = 4
**Output:** 4

#### Notes
Notes are here [[K Largest Element in an Array]]

#### Code
**Time Complexity**:
**Space Complexity**: 

```go
import "container/heap"

func findKthLargest(nums []int, k int) int {
    minHeap := &IntHeap{}
    heap.Init(minHeap)
    for _, n := range nums {
        heap.Push(minHeap, n)
        if minHeap.Len() > k {
            heap.Pop(minHeap)
        }
    }
    return minHeap.Peek()
}

type IntHeap []int
func (h IntHeap) Len() int { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h IntHeap) Peek() int { return h[0] }
func (h *IntHeap) Push(x any) {
    *h = append(*h, x.(int))
}
func (h *IntHeap) Pop() any {
    prev := *h
    n := len(prev)
    x := prev[n-1]
    *h = prev[:n-1]
    return x
}

```


#### Follow Up: *""*

```python

```