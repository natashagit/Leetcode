class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map_dict:
                return [map_dict[diff], i]
            map_dict[nums[i]]=i
        