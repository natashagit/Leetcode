class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # input: list of heights
        # output: max area between two edges
        # area= difference btwn the edges*height of the shorter edge
        # two pointer approach
        # left and right pointer
        # max_area initialized
        # while left< right
        # if height of left<height of right-> area formula=heigh of left*(right-left pointer) -> store max_area
        # return max_area

        left = 0
        right = len(height)-1
        max_area = 0
        while left<right:
            if height[left]<height[right]:
                area = height[left]*(right-left)
                left+=1
            else:
                area = height[right]*(right-left)
                right-=1
            max_area = max(area, max_area)
        return max_area