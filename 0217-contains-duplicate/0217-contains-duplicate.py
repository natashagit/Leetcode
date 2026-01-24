class Solution(object):
    # input: array nums
    # output: if more than 1 occurrence of any value in nums, return True
    # use dict
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # input: nums array
        # output: true - if an element repeated, else false
        # keep a set and add values to set and if seen then return false
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        