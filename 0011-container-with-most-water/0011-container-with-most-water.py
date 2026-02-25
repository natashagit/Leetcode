class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # input: array of heights
        # output: max area of water between two heights
        # height-> 0, -ve, only one height -> return 0 area
        # input size ->10^5 -> O(n) 
        l = 0
        r = len(height)-1
        max_area = 0
        while l<r:
            area = (r-l)*min(height[l], height[r])
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            max_area = max(max_area, area)
        return max_area