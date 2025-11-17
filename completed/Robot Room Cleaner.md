---
tags:
  - hard
  - backtracking
  - meta
link: https://leetcode.com/problems/robot-room-cleaner/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
last_attempt: 2025-11-17
rate:
  - ★★★★
---
#### Variants

#### Problem
You are controlling a robot that is located somewhere in a room. The room is modeled as an `m x n` binary grid where `0` represents a wall and `1` represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API `Robot`.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is `90` degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

```
interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
```

**Note** that the initial direction of the robot will be facing up. You can assume all four edges of the grid are all surrounded by a wall.

**Custom testing:**

The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/17/lc-grid.jpg)

**Input:** `room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3`
**Output:** Robot cleaned all rooms.
**Explanation:** All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.

**Example 2:**

**Input:** room = [[1]], row = 0, col = 0
**Output:** Robot cleaned all rooms.
#### Notes
We continuously travel in the forward direction until we hit an obstacle, in which case we turn right. 

We backtrack when we hit a dead end by turning around and moving in that direction the pointing the robot in the forward direction again.

We need to keep track of the current direction in our backtrack recursive call because forward is relative to which direction we are facing.

>[!example]
>If we are current looking south, then forward is south.

#### Code
**Time Complexity**: O(N - M), where N is total cells and M is obstacles
**Space Complexity**: O(N - M), for visited set

```python
class Solution:
    def cleanRoom(self, robot):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def reverse():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def travel(cell, curdir):
            visited.add(cell)
            robot.clean()
            x, y = cell
            for i in range(4):
                # On the first iteration this should 
                # face the same direction as the parent
                # Bc we want to continue going in the 
                # same direction in a straight line if we can
                newdir = (i + curdir) % 4
                dx, dy = directions[newdir]
                newcell = (x + dx, y + dy)
                # Keep recursively traversing until we hit it a deadend
                # in which case we reverse and come back up and try the
                # "right" (relative to current direction)
                if newcell not in visited and robot.move():
                    travel(newcell, newdir)
                    reverse()
                robot.turnRight()
        travel((0, 0), 0)
```
