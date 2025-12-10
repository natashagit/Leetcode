class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: array
        # output: element that is majority

        # keep a count in dict for every element, when it crosses >n/2 return that element
        dict_nums = {}
        for i in range(len(nums)):
            if nums[i] in dict_nums:
                dict_nums[nums[i]]+=1
                if dict_nums[nums[i]]>(len(nums)/2):
                    return nums[i]
            else:
                dict_nums[nums[i]]=1
        return nums[i]
        