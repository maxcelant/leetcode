#### Fundamental
- You always want to add to the visited set when you enqueue/push the node. 
- Path finding / Exploration BFS problems, always figure out what you need to initialize the array with!
	- Examples:
		- [[Rotten Bananas]] — queueing all the rotten bananas and counting fresh
		- [[Islands and Treasures]] — queueing all the treasure locations
- 

#### Level Order BFS
- To perform true level order bfs, you need to loop through the queue all at once.

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

