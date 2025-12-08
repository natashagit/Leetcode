class Solution(object):
    # input: array nums
    # output: if more than 1 occurrence of any value in nums, return True
    # use dict
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        