class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # restate problem:
        # input: array + target value
        # output: indexes whose values sum up to the target
        # assumptions:
        # duplicates allowed
        # negative yes
        # no match - return empty array
        dict_map = {} # [-3, 4, 3] , 0
        for i in range(len(nums)): #-3
            if (target - nums[i]) in dict_map:
                return [i, dict_map[(target - nums[i])]] #[2,1]
            dict_map[nums[i]] = i # {3:0, 2:1}
        return []
