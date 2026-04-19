class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: nums
        # output: pivot index: left elements=right elements of pivot index
        total_sum = sum(nums)
        pref_sum=0
        for i in range(len(nums)):
            if total_sum-pref_sum-nums[i]==pref_sum:
                return i
            pref_sum+=nums[i]
        return -1