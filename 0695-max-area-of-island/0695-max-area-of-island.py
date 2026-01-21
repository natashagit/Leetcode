class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # input: grid
        # output: max area of an island, else 0 if no island
        # Use dfs to track islands, 
        # take sum for area

        rows, cols = len(grid), len(grid[0])
        visit = set()
        max_area = 0
        area = 0
        def dfs(i, j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!=1 or (i,j) in visit:
                return 0
            visit.add((i,j))
            return (1+ dfs(i, j+1) + dfs(i, j-1) + dfs(i+1, j) + dfs(i-1, j))
              
        for r in range(rows):
            for c in range(cols):
                area = dfs(r, c)
                max_area = max(area, max_area)
        return max_area
                    