class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: array nums
        # output: largest sum of the subarray
        # constraints:not gonna be empty [], negative only is possible
        # initialize maxsum=nums[0], currsum = nums[0]
        # loop through nums
        # update currsum to max of element in nums vs currsum+element
        # update maxsum to largest cursum
        maxsum = nums[0]
        currsum = nums[0]
        for i in range(1, len(nums)):
            currsum = max(nums[i], currsum+nums[i])
            maxsum = max(maxsum, currsum)
        return maxsum