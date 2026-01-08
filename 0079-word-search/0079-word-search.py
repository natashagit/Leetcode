class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        # so that no revisiting the char on board
        path = set() 
        def dfs(r, c, i):
            if i ==len(word):
                return True
            #  out of bounds, character not on board, character visited before
            if (r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] or (r,c) in path):
                return False
            # Add visited to path
            path.add((r,c))
            # Run dfs to find in all 4 directions
            res = (dfs(r+1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c-1, i+1))

            # Remove visited from path since now visited all from start
            path.remove((r,c))
            return res
        
        # Looping through matrix and running dfs for each char
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
        