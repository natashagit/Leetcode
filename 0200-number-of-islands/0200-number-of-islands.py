class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # input: mXn matrix
        # output: number of islands
        # number of components
        # DFS and everytime it breaks, increase count of islands
        r,c = len(grid), len(grid[0])

        def dfs(i,j):
            if i<0 or i>=r or j<0 or j>=c or grid[i][j]!='1':
                return
            # convert to water since not visiting again
            grid[i][j]='0'
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i,j-1)
            dfs(i-1, j)
        
        num_islands = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    num_islands+=1
                    dfs(i,j)
        return num_islands