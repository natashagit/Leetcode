class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # input: grid containing 2:rotten, 1:fresh, 0: no oranges
        # output: return steps until all oranges traversed
        # Use BFS for level by level traversal
        # need to add all rotten oranges to queue
        # each level-1 minute - time increment
        # track fresh oranges - everytime rots- decrement
        # if fresh oranges> 0 in end- return -1
        # else return time
        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        from collections import deque
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh_oranges+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        if fresh_oranges==0:
            return 0
        time = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        while q and fresh_oranges>0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc + c
                    if nr>=0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh_oranges-=1
                        q.append((nr,nc))
            time+=1
        
        return time if fresh_oranges==0 else -1
        
        

        