class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: nums array
        # output: pivot index which equally divides with sum equal on both sides of pivot, else -1
        # constraints: array size 1, negative numbers
        # edge cases: one element, index return 0
        # take sum of all elements
        # left sum assign to 0
        # loop through nums
        # check if sum-left sum-pivot == left sum
        # if yes then return pivot
        # else increase left sum by adding element to it

        left_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            if total_sum-left_sum-nums[i] == left_sum:
                return i
            left_sum+=nums[i]
        return -1
