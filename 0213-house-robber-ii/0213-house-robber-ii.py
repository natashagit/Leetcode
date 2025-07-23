class Solution:
    def rob(self, nums: List[int]) -> int:
        # taking edge case of nums having only 1 element as well
        # Taking max of subarrays without 1st and last element: since circle
        return max(nums[0], self.prev_rob(nums[1:]), self.prev_rob(nums[:-1]))
      
    def prev_rob(self, nums):
        rob1, rob2 = 0, 0 
        for n in nums:
            # [rob1, rob2, n, n+1, ...]
            # rob1 and n can be taken together, or else just rob2
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2