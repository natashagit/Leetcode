class Solution(object):
   
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 0s exist
        # negatives exist
        left_product = [1]*len(nums)
        right_product = [1]*len(nums)
        run_prod = 1
        final = []
        n = len(nums)
        for i in range(1, n):
            left_product[i] = left_product[i-1]*nums[i-1]
            right_product[n-i-1] = right_product[n-i]*nums[n-i]
        for i in range(n):
            final.append(left_product[i]*right_product[i])
        return final

