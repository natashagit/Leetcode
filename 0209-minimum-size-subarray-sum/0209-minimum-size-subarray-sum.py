class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # input: nums array, target
        # output: minimum length of the array that has a sum>=7, else 0
        # window -> add elements to the window on the right till sum>=7
        # note the size of window
        # remove element from window from the left
        window = 0
        left = 0
        length = 0
        min_length = float("inf")
        right = 0
        while right<len(nums):
            window+=nums[right]
            while window>=target:
                length = right - left + 1
                min_length = min(length, min_length)
                window-=nums[left]
                left+=1
            right+=1
            
        return 0 if min_length==float("inf") else min_length
