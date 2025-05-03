- You always want to add to the visited set when you enqueue/push the node. 
- With Pathfinding / Exploration BFS problems, always figure out what you need to initialize the array with!
	- Examples:
		- [[problems/Rotten Bananas|Rotten Bananas]] — queueing all the rotten bananas and counting fresh
		- [[problems/Islands and Treasures|Islands and Treasures]] — queueing all the treasure locations
- When I read **"undirected graph"**, I should remember that I need to add each others values to the adjacency list.
	- Examples:
		- [[Valid Tree]]
		- [[Number of Connected Components in an Undirected Graph]]
- When I read **"undirected graphs"**, I should remember to skip the parent in the traversal.
	- Examples:
		- [[Valid Tree]]
		- [[Number of Connected Components in an Undirected Graph]]
- I want to get a path from the bottom up, then I need to add the nodes in a "post-order" fashion.
	- Examples:
		- [[Course Schedule II]] — We need to build the dependencies in order from the one that doesn't have any to the most dependent.
#### Specific Algorithms
##### Level Order BFS
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

