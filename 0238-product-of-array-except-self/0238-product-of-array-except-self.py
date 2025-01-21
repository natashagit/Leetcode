class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = [1]
        # Using postfix and prefix for values before and after
        prefix = 1
        for i in range(len(nums)-1):
            result.append(nums[i]*prefix)
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = result[i]*postfix
            postfix*=nums[i]

        return result