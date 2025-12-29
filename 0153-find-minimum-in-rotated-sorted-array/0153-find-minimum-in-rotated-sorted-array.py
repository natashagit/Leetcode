class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: rotated sorted array
        # output: minimum element in that rotated sorted array

        # binary search
        # we can return the minimum in the sorted part of the array
        # set min_value to nums[0]
        # we can set lowptr as 0
        # we can set highptr as len(nums)
        # we can take the midpt -> take lower value
        # check if the midpt is higher than lowptr value
            # set the min_value as low's value
            # set low to midpt+1
        # if no, then
            # set the min_value as midpt's value
            # set high to midpt-1
        # return min_value
            # 4 5 6 0 1 2 
        
        min_value = nums[0]
        lowptr = 0
        highptr = len(nums)-1

        while lowptr<=highptr:
            midpt = (lowptr+highptr)//2
            if nums[midpt]>=nums[lowptr]:
                min_value = min(min_value, nums[lowptr])
                lowptr = midpt+1
            else:
                min_value = min(min_value, nums[midpt])
                highptr = midpt-1
        return min_value