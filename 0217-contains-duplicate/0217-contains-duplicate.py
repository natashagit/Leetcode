class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_nums = {}
        for i in nums:
            if i not in count_nums:
                count_nums[i]=1
            else:
                return(True)
        return(False)