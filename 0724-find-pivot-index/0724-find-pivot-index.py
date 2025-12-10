class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: nums array
        # output: pivot index
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total-left_sum-nums[i]:
                return i
            left_sum+=nums[i]
        
        return -1
        
