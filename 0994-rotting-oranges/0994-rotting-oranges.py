class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # put all rotten oranges in queue as (r,c,time it becomes rotten-initally 0)
        # keep a visited set to store the r, c of the rotten oranges
        # do a bfs and keep updating time as new oranges get rotten and add r,c of new oranges to visited
        # if fresh oranges still left -> return -1
        # return the maximum time it takes to make all oranges rotten
        
        
        from collections import deque

        rotten_oranges = deque()
        time = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    rotten_oranges.append((r,c, 0))
                    visited.add((r,c))
        directions = [[0,1], [1,0], [0,-1], [-1, 0]]
        while rotten_oranges:
            r,c,t = rotten_oranges.popleft()
            time = max(t, time)
            for dr,dc in directions:
                new_r = r+dr
                new_c = c+dc
                if new_r>=0 and new_r<rows and new_c>=0 and new_c<cols and grid[new_r][new_c]==1 and (new_r, new_c) not in visited:
                    rotten_oranges.append((new_r, new_c, t+1))
                    visited.add((new_r, new_c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    return -1 
        
        return time


        
