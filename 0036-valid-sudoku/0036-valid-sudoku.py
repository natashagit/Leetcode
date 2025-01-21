class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n_rows = len(board)
        n_cols = len(board[0])
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j]=='.':
                   continue
                sqind = (i // 3) * 3 + (j // 3)
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                if board[i][j] in squares[sqind]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[sqind].add(board[i][j])
        return True
                
