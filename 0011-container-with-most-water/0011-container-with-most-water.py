class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = 0
        b = len(height) -1
        max_area = 0
        while a<len(height) and b>0:
            if height[a]<height[b]:
                area = height[a]*(b-a)
                a+=1
            else:
                area = height[b]*(b-a)
                b-=1
            if area>max_area:
                max_area = area
        return max_area

