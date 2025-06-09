class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Taking maximum subarray as max of list initially
        maxSub = max(nums)
        # Keep track of current sum
        currSum = 0
        for n in nums:
            # If current sum goes lesser than 0, set to 0
            if currSum<0:
                currSum = 0
            currSum+=n
            # Take maximum sum of subarray
            maxSub = max(maxSub, currSum)

        return maxSub