class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time Complexity= O(n)
        dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in dict:
                dict[nums[i]] = i
            else:
                return [dict[diff], i]

        # Time Complexity = O(n^2)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
       

        