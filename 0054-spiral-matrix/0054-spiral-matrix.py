class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # input 2D matrix
        # output: 1D list of spiral
        # 1d array list, 
        # while top, bottom, right, left boundaries keep reducing
        # add elements to result array
        # from left to right and top to bottom

        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        result = []
        while top<=bottom and left<=right:
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top+=1
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right-=1
            # check if line present as top increased
            if top<=bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom-=1
            # check if line present as right reduced
            if left<=right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left+=1
        return result
