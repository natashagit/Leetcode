class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: array
        # output: max sum
        # max_sum
        # loop through nums
        # add values-> if its less than 0 make it 0
        # store each time the sum as max_sum by taking max

        max_sum = max(nums)
        sum_value = 0
        for i in nums:
            if sum_value<0:
                sum_value=0
            sum_value +=i
            max_sum = max(max_sum, sum_value)
        return max_sum
