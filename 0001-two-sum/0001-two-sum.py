class Solution(object):
    # input: nums array, target
    # output: indices of two values in nums that add up to target
    # dictionary -> value: index
    # we check if the value subtracted from the target is there in the dictionary, if so we retur, the value for that key in the dict and the current index
    # if the index!=the value: same element
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # input: nums array, target
        # output: index of two numbers that add up to target
        # dictionary
        # init dict
        # loop through array
        # if target-nums[i] in dict then return i and dict[num[i]]
        # else add dict[nums[i]]=i to dict
        dict_num={}
        for i in range(len(nums)):
            if target-nums[i] in dict_num:
                return [i, dict_num[target-nums[i]]]
            else:
                dict_num[nums[i]]=i
        