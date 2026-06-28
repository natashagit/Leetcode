class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: rotated input array
        # output: minimum value
        # [2,4,5,6,7,0,1]
        low = 0
        high = len(nums)-1
        while low<high:
            mid_pt = (low+high)//2
            if nums[mid_pt]>nums[high]:
                low = mid_pt+1
            else:
                high = mid_pt
        return nums[low]