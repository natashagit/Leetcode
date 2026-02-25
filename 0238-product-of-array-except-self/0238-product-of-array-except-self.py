class Solution(object):
   
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result_product = [1 for i in range(len(nums))]
        prefix = 1
        for i in range(len(nums)):
            result_product[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result_product[i] = result_product[i]*suffix
            suffix = suffix * nums[i]
    
        
        return result_product