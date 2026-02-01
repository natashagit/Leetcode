class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # input: nums
        # output: largest product in subarray
        # initialize max product to max of elements in nums
        # can be two negatives-> positive
        currMax, currMin = 1,1
        max_product = max(nums)
        for num in nums:
            temp = num*currMax
            currMax = max(num*currMax, num*currMin, num)
            currMin = min(temp, num*currMin, num)
            max_product = max(max_product, currMax)
        return max_product


        