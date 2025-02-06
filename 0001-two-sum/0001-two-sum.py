class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in dict:
                dict[nums[i]] = i
            else:
                return [dict[diff], i]

       

        