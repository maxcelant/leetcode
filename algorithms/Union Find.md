- You can do a rank based union find or a size based union find.
	- `rank`: is determined by the height of the tree.
		- Example: [[Redundant Connection]]
	- `size`: is determined by number of nodes in that tree.
		- Example: [[Min Cost to Connect Points]]

```python
parent = list(range(n))
rank = [0] * (n)

def find(x):
	node = x
	while node != parent[node]:
		node = parent[node]

	# (optimization not really necessary)
	while x != node:
		temp = parent[x]
		parent[x] = node
		x = temp

	return node

def union(u, v):
	ru, rv = find(u), find(v)

	# Parents are the same! cycle found
	if ru == rv:
		return False

	if rank[ru] < rank[rv]:
		parent[ru] = rv
	elif rank[ru] > rank[rv]:
		parent[rv] = ru
	else:
		parent[rv] = ru
		rank[ru] += 1
	return True
```

#### Problems
- [[Min Cost to Connect Points]]
- [[Redundant Connection]]