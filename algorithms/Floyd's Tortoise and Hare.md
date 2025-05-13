This algorithm is used to find a cycle in a list / linked list.

```python title:"List approach"
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
				
        start = 0
        while True:
            slow = nums[slow]
            start = nums[start]
            if slow == start:
                return slow
```

```python title:"Linked list approach"
class Solution:
    def findDuplicate(self, head: ListNode) -> int:
		fast = slow = head
		while True:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				break

		start = head
		while True:
			start = start.next
			slow = slow.next
			if slow == start:
				return slow
```

The algorithm can be broken down into two parts:
1. Finding the crux: First we use a fast and slow pointer to find the node that begins the cycle.
2. Finding the intersection: We then start one pointer from the beginning of the list and the other from the crux. We move each forward until they meet.

#### Problems
- [[Find the Duplicate Number]]