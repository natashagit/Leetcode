class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # input: nums, target
        #   output: indices of two values in nums that add up to target
        # constraints: can have negative and 0
        # edge cases: same number - different indices, negative numbers
        # dictionary to store the elements seen with its index
        # loop through nums and check if the target-element in nums is there in dictionary
        # if its there then we want to return the index and the value of the item in the dictionary
        # else add to dictionary

        dict_nums = {}
        for i in range(len(nums)):
            if target-nums[i] in dict_nums:
                return [i, dict_nums[target-nums[i]]]
            dict_nums[nums[i]]=i
        






    