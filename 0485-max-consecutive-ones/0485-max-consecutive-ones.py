class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        max_length = 0
        for r in range(len(nums)):
            if nums[r]==1:
                max_length = max(max_length, r-l+1)
            else:
                l = r+1
        return max_length