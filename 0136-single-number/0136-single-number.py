class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: array of nums
        # output: unique number
        # XOR elements to get the unique number
        result = 0
        for num in nums:
            result = result^num
        return result
