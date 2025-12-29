class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # input: matrix, target value
        # output: true/false if target present in matrix
        # edge cases: empty matrix

        # binary search since in ascending order

        # left pointer at beginning of matrix
        # right pointer at end of matrix row
        # while left<right
        # check if target<value at right
            # if yes, midpt = left+right/2
            # check if target<value at midpt
            # if yes right=midpt-1
            # if no left = midpt+1
            # else:
            # return True
        # if no, set left to next row beginning and right to end of next row

        # return False
        i=0
        while i<len(matrix):
            left = 0
            right = len(matrix[0])-1
            if target>matrix[i][right]:
                i+=1
                continue

            while left<=right:
                midpt = (left+right)/2
                if target<matrix[i][midpt]:
                    right = midpt-1
                elif target>matrix[i][midpt]:
                    left = midpt+1
                else:
                    return True
            return False

        return False