class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # input: nums, target
        # output: minimum length of subarray whose sum is>=target
        # nums all elements are positive
        # two pointer approach and keep window
        # left at start
        # right move through nums
        # if the sum upto right>=target -> shrink window from left and keep count of the size-> r-l 
        left = 0
        curr_sum = 0
        result_len = float("inf")
        for right in range(len(nums)):
            curr_sum+=nums[right]
            while curr_sum>=target:
                result_len = min(result_len, right-left+1)
                curr_sum-=nums[left]
                left+=1
        if result_len==float("inf"):
            return 0
        else:
            return result_len
                
        
        