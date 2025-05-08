To perform true level order bfs, you need to loop through the queue all at once.

```python
Q = deque([])
level = 0

while Q:
	for _ in range(len(Q)):
		node = Q.popleft()
		for neighbor in node.neighbors:
			if neighbor not in visited:
				visited.add(neighbor)
				Q.append(neighbor)
		level = level + 1
```

