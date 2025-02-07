class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]*len(nums)
        right = [1]*len(nums)
        result = []
        
        # Take product of all elements to the left
        for i in range(1, len(nums)):
            left[i] = nums[i-1]*left[i-1]
        # Take product of all elements to the right
        for i in range(len(nums)-2, -1, -1):
            right[i] = nums[i+1]*right[i+1]
        # Take pairwise product of both
        for i in range(len(nums)):
            result.append(left[i]*right[i])

        return result