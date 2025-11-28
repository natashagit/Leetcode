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
        dict_nums = {}
        for i in range(len(nums)):
            if (target-nums[i]) in dict_nums:
                return [i, dict_nums[target-nums[i]]]
            else:
                dict_nums[nums[i]]=i
        