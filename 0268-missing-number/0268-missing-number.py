class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Need to consider last element in the difference btwn sums
        sum_res = len(nums)

        # Taking the difference between the two sums of arrays to get missing/remaining value
        for i in range(len(nums)):
            sum_res +=(i-nums[i])
        return sum_res

        # Extra space of O(n)
        # a = set(nums)
        # for n in range(len(nums)+1):
        #     if n not in a:
        #         return n
        # return
        
        