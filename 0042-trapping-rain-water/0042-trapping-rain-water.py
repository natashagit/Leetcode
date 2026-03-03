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
        # TC: O(n) and SC: O(n)
        
        # if len(height)<=1:
        #     return 0
        # maxLeft = [0]*len(height)
        # maxRight = [0]*len(height)
        # maxLeft[0] = height[0]
        # maxRight[len(height)-1] = height[len(height)-1]
        # area = 0

        # for i in range(1, len(height)):
        #     maxLeft[i] = max(maxLeft[i-1], height[i])
        # for i in range(len(height)-2, -1, -1):
        #     maxRight[i] = max(maxRight[i+1], height[i])
        
        # for i in range(len(height)):
        #     area+=min(maxLeft[i], maxRight[i])-height[i]
        # return area


        # SC: O(1) soln
        left = 0
        right = len(height)-1
        maxLeft = 0
        maxRight = 0
        area = 0
        while left<right:
            if height[left]<=height[right]:
                maxLeft = max(height[left], maxLeft)
                area+= (maxLeft-height[left])
                left+=1
            else:
                maxRight = max(height[right], maxRight)
                area+= (maxRight-height[right])
                right-=1
        return area