class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n-1
        top, bottom = 0, m-1 
        result = []
        while(top<=bottom and left<=right):
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top+=1
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right-=1
            # Check needed if only one line, top increased
            if top<=bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom-=1
            # Check needed if no top line to be printed in end
            if left<=right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left+=1
        return result
        
        