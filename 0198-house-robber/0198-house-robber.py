class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # store max amount of money we can rob up until the index
        # input: nums array
        # output: max amount robber - no adjacent houses allowed
        # [2 1 1 3] = 5 
        #  2 2 3 5 -> 5
        # nums[i] = max(nums[i] + nums[i-2], nums[i-1])

        for i in range(1, len(nums)):
            if i == 1:
                nums[i] = max(nums[i-1], nums[i])
            else:
                nums[i] = max(nums[i] + nums[i-2], nums[i-1])
        return nums[-1]

