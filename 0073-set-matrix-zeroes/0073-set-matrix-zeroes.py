class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # input: matrix
        # output: inplace modify matrix based on zeroes
        # loop through matrix and check if element is 0
        # if its 0-> set all elements in a copy in that row and column to 0 : O(m.n) space
        # keep one row and col array and set to 0 based on matrix: O(m+n) space
        # first row and column in matrix to be kept for storing row and col for 0: O(1) space

        m = len(matrix)
        n = len(matrix[0])
        rowZero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    else:
                        rowZero = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0]==0:
            for i in range(m):
                matrix[i][0] = 0
        
        if rowZero:
            for j in range(n):
                matrix[0][j]=0
        

