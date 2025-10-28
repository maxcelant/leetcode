---
tags:
  - nvidia
  - medium
  - linked-list
link: https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=company&envId=nvidia&favoriteSlug=nvidia-six-months
last_attempt: 2025-10-26
rate:
  - ★★★★
---
#### Variants
- [[Clone Graph]]

#### Problem
A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return _the head of the copied linked list_.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will **only** be given the `head` of the original linked list.

#### Notes
Notes can be found here [[Copy Linked List with Random Pointer]].

#### Code
**Time Complexity**: O(N)
**Space Complexity**: O(N)

```python
func copyRandomList(head *Node) *Node {
    clones := map[*Node]*Node{}
    var traverse func(*Node) *Node
    traverse = func (cur *Node) *Node {
        if cur == nil {
            return nil
        }
        if n, ok := clones[cur]; ok {
            return n
        }
        newNode := &Node{cur.Val, nil, nil}
        clones[cur] = newNode
        newNode.Next = traverse(cur.Next)
        newNode.Random = traverse(cur.Random)
        return newNode
    }
    return traverse(head)
}
```


#### Follow Up: *""*

```python

```