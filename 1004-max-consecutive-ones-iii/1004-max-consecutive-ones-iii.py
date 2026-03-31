class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # input: nums array, k
        # output: length of longest subarray containing 1's after changing max k 0's
        # window adding on right
        # if element 1, add on
        # if element 0, reduce from k
        # when k=0-> move left ahead
        right = 0
        left = 0
        max_ones = 0
        while right<len(nums):
            if nums[right]==0:
                k-=1
            while k<0:
                if nums[left]==0:
                    k+=1
                left+=1
            max_ones = max(max_ones, right-left+1)
            right+=1
        return max_ones
            
            