class Solution(object):
   
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product = [1 for i in range(len(nums))]
        right_product = [1 for i in range(len(nums))]
        final_product = []

        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right_product[i] = right_product[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            final_product.append(left_product[i] * right_product[i])
        
        return final_product