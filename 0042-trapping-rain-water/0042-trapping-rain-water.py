class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # input: heights list
        # output: sum of area of water filled
        # calculate max_left and max_right at every point
        # calculate area at point by taking min of max_left and max_right and subtract the current height from it to get area
        max_left = [0]*len(height)
        max_right = [0]*len(height)

        max_left[0] = height[0]
        max_right[len(height)-1]=height[len(height)-1]

        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i-1])
        
        for i in range(len(height)-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])
            
        area = 0
        for i in range(len(height)):
            area += min(max_left[i], max_right[i])-height[i]
        return area
