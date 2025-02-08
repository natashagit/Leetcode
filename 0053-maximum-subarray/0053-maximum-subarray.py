class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cnt_sum = 0
        for i in range(len(nums)):
            cnt_sum+=nums[i]
            if cnt_sum>max_sum:
                max_sum=cnt_sum
            if cnt_sum<0:
                cnt_sum=0
            
        return max_sum
