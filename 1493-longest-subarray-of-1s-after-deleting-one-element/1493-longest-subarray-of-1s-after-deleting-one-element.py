class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: nums
        # output: max length of subarray (1's) after deleting one element
        # everytime we encounter a 0, we store that location and move the left ahead of it
        # and we update max_length -> right-left
        zero = -1
        left = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right]==0:
                left = zero + 1
                zero = right
            max_len = max(max_len, right-left)
        return max_len

