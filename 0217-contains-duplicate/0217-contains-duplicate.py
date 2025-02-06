class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict_={}
        for i in range(len(nums)):
            if nums[i] in dict_:
                return True
            else:
                dict_[nums[i]]=1
        return False