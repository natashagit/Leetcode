class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: nums array
        # output: number that is not present in the range
        # take XOR of all elements in nums and XOR of all elements in range
        # take XOR of both
        # get unique number
        n = len(nums)
        result = 0
        for i in range(0,n+1):
            result^=i
        for num in nums:
            result^=num
        return result
            