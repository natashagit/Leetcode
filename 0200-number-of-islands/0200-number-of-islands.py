class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        # Keep count of locations visited
        visit = set()
        islands = 0

        def bfs(r,c):
            # vertical and horizontal from r,c
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            from collections import deque
            q = deque()
            visit.add((r,c))
            q.append((r , c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    #index of row and col in directions
                    rr, cc = row+dr, col+dc
                    #check if row, col in range, element is 1, not visited
                    if (rr in range(rows) and cc in range(cols) and grid[rr][cc]=="1" and (rr,cc) not in visit):
                        visit.add((rr,cc))
                        q.append((rr, cc))


        # loop through grid
        for r in range(rows):
            for c in range(cols):
                # check for 1 in grid and if not visited, do bfs to get all 1s of that island and increment number of islands
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        
        return islands