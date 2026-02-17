class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # input: matrix
        # output: rotated matrix
        # constraints: inplace
        # transpose and reverse
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(m):
            matrix[i] = matrix[i][::-1]
        return matrix