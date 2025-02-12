class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Time Complexity = O(mn) # Space Complexity= O(m+n)
        m = len(matrix)
        n = len(matrix[0])
        # To Keep track of rows and cols with 0 
        rows = [False]*m
        cols = [False]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
        return matrix