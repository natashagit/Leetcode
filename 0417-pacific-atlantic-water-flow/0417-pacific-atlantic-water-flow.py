class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS =len(heights), len(heights[0])
        # Keep a set for vlues reaching pacifici and atlantic
        pac, atl = set(), set()

        # Function to search depth wise from the ocean onwards, for each cell(r,c), visit-> visited cells, prevHeight -> keep check of descending order towards sea
        def dfs(r, c, visit, prevHeight):
            # Check for cell in visited, cell out of bound, cell not in descending order
            if ((r,c) in visit or r<0 or c<0 or r==ROWS or c==COLS or heights[r][c]<prevHeight):
                return
            # Since it passes all conditions it is added to the visited
            visit.add((r,c))

            # Run it recursively for rest of the cells in N,S,E,W directions from the sea
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        # Start check for pacific from top and atlantic from bottom
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        # Start check for pacific from left and atlantic from right
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        # Get result having values in both pac and atl
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res

