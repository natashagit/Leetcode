class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # input: heights of the walls
        # output: total water trapped between the walls
        # no negative values
        # one wall -> 0
        # no wall -> 0
        # brute force
        # So we take the maximum height on left and right and subtract the current index height from the minimum of the left and right heights to get the area
        # O(n^2) - scanning left and right for maximum
        # maxLeft = 0
        # maxRight = 0
        
        # total_water = 0
        # for i in range(len(height)):
        #     maxLeft = max(height[:i+1])
        #     maxRight = max(height[i:])
        #     total_water += min(maxLeft, maxRight)-height[i]
        # return total_water

        # Optimal
        maxLeft = height[0]
        maxRight = height[len(height)-1]
        left = 0
        total = 0
        right = len(height)-1
        while left<right:
            if maxLeft <maxRight:
                total += maxLeft-height[left]
                left+=1
                maxLeft = max(height[left], maxLeft)
            else:
                total += maxRight-height[right]
                right-=1
                maxRight = max(height[right], maxRight)
        return total




            
            