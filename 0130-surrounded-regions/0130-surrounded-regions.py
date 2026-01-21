class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # input: board with X and O's
        # output: return board surrounded, O's if not surrounded since touching border
        # find the O's connected to the border, flip the rest
        # start from border cell
        # if it is 0, do bfs and mark all connected as safe
        # after marking flip all remaining O's to X
        # turn safe back to O's
        rows, cols = len(board), len(board[0])
        from collections import deque
        
        def bfs(i, j):
            if i<0 or j<0 or i>=rows or j>=cols or board[i][j]!='O':
                return
            board[i][j] = "S"
            q = deque()
            q.append((i, j))
            directions = [(1,0),(-1,0), (0,1), (0,-1)]
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr, nc = dr+r, dc+c
                    if nr>=0 and nr<rows and nc>=0 and nc<cols and board[nr][nc]=='O':
                        board[nr][nc]='S'
                        q.append((nr,nc))
                

        for r in range(rows):
            bfs(r, 0)
            bfs(r, cols-1)
        for c in range(cols):
            bfs(0,c)
            bfs(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="S":
                    board[r][c]="O"