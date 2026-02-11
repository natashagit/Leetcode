class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # input: heights list
        # output: max area between two heights in heights
        # left and right ptrs
        # area = maximize->min height(left height, right height)*right-left+1
        # if left height<right height->left+=1
        # else right-=1
        left = 0
        right = len(height)-1
        max_area = float("-inf")
        while left<right:
            max_area = max(max_area, (right-left)*min(height[left], height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area









       