class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # input: list of heights
        # output: total area of water trapped in between
        # height-> 0, -ve, one one element in height
        # input size->10^4 O(n)
        # water limited by tallest wall on left or right of it
        # min of maxleft, maxright at every point will determine the area at that point
        # keep an array to store maxleft elements
        # keep an array to store maxright elements
        # create maxleft array by looping from start and storing maxvalue seen at every index
        # create maxright array by looping form end and storing maxvalue seen at every index
        # finally calculate the area by summing up the area at every index by taking the minimum of maxleft and maxright and reducing the current index height from it

        maxLeft = [0]*len(height)
        maxRight = [0]*len(height)
        maxLeft[0] = height[0]
        maxRight[len(height)-1] = height[len(height)-1]
        area = 0

        for i in range(len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i])
        for i in range(len(height)-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])
        
        for i in range(len(height)):
            area+=min(maxLeft[i], maxRight[i])-height[i]

        return area