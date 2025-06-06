class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.matrix_sum = [[0]*(cols+1) for r in range(rows+1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix+=matrix[r][c]
                above = self.matrix_sum[r][c+1] 
                self.matrix_sum[r+1][c+1] = prefix+above #Adding all that is above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        bottomRight = self.matrix_sum[row2][col2]
        above = self.matrix_sum[row1-1][col2]
        left = self.matrix_sum[row2][col1-1]
        topLeft = self.matrix_sum[row1-1][col1-1]

        return bottomRight - above - left + topLeft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)