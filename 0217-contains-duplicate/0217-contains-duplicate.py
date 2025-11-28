class Solution(object):
    # input: array nums
    # output: if more than 1 occurrence of any value in nums, return True
    # use dict
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict_nums = {}
        for i in nums:
            if i in dict_nums:
                return True
            else:
                dict_nums[i]=1
        return False
        