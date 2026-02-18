class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: nums list
        # output: max number of consecutive ones
        # 
        current = 0
        max_length = 0
        for i in range(len(nums)):
            if nums[i]==1:
                current+=1
                max_length = max(max_length, current)
            else:
                current=0
        return max_length