class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
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